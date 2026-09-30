"""The course service: one small task API, standard library only.

`App.dispatch` is a router in the plainest possible shape, because every lesson
in this course reads lines of it on screen. The boundaries of the teaching lab
are named where they happen: the websocket route completes a handshake and
stops there, the token routes sign with a local key that is in this file, and
the store is an in-memory SQLite database seeded from seeds.json on every
start, so two runs of the same request give the same answer.

Faults live in breakages/ as patches against this file, never as switches
inside it. What you read here is the correct behaviour.
"""
import base64
import hashlib
import hmac
import json
import sqlite3
import threading
import time
from http import HTTPStatus
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import miniyaml

ROOT = Path(__file__).resolve().parent
SPEC = miniyaml.load((ROOT / 'openapi.yaml').read_text())
LIMIT_MAX = SPEC['paths']['/tasks']['get']['parameters'][0]['schema']['maximum']
SORTS = {'id': 'id', 'title': 'title,id', '-title': 'title DESC,id'}
FIELDS = {'id', 'title', 'state'}

# Local teaching keys. Real deployments read these from a secret store; the
# point on screen is the rotation mechanism, so both generations are present.
KEYS = {'current': b'local-teaching-key-not-a-secret',
        'previous': b'previous-local-teaching-key'}
WEBHOOK_KEY = b'local-webhook-key'


def encode(raw):
    """Base64url without padding, which is what JWT uses."""
    return base64.urlsafe_b64encode(raw).rstrip(b'=').decode()


def decode(text):
    return base64.urlsafe_b64decode(text + '===')


def token(kid='current', **claims):
    """Mint a signed token. The course never ships a token it did not sign."""
    header = encode(json.dumps({'alg': 'HS256', 'kid': kid}).encode())
    body = {'sub': 'alice', 'iss': 'course', 'aud': 'tasks',
            'exp': 4102444800, 'scope': 'tasks:read', **claims}
    payload = encode(json.dumps(body).encode())
    signing_input = f'{header}.{payload}'
    return signing_input + '.' + sign(KEYS[kid], signing_input)


def sign(key, signing_input):
    return encode(hmac.digest(key, signing_input.encode(), 'sha256'))


def identity(value):
    """Claims from a bearer token, or None. Signature first, then claims."""
    try:
        header_b64, payload_b64, signature = value.split('.')
        header = json.loads(decode(header_b64))
        claims = json.loads(decode(payload_b64))
        if header.get('alg') != 'HS256' or header.get('kid') not in KEYS:
            return None
        expected = sign(KEYS[header['kid']], f'{header_b64}.{payload_b64}')
        if not hmac.compare_digest(signature, expected):
            return None
        if claims.get('iss') != 'course' or claims.get('aud') != 'tasks':
            return None
        if claims.get('exp', 0) <= time.time():
            return None
        return claims
    except (ValueError, KeyError, TypeError):
        return None


class App:
    def __init__(self):
        self.lock = threading.RLock()
        self.db = sqlite3.connect(':memory:', check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
        CREATE TABLE owners(id TEXT PRIMARY KEY, name TEXT);
        CREATE TABLE tasks(id INTEGER PRIMARY KEY, title TEXT, state TEXT,
                           owner TEXT, revision INTEGER DEFAULT 1);
        INSERT INTO owners VALUES ('alice','Alice'),('bob','Bob');
        ''')
        seeds = json.loads((ROOT / 'seeds.json').read_text())
        self.db.executemany(
            'INSERT INTO tasks(id,title,state,owner) VALUES (?,?,?,?)',
            [(s['id'], s['title'], s['state'], s['owner']) for s in seeds])
        self.db.commit()
        self.replays = {}
        self.events = []
        self.seen = set()
        self.calls = 0
        self.metrics = []
        self.queries = 0

    # ---- helpers -------------------------------------------------------

    def problem(self, status, detail=None, headers=None):
        """RFC 9457, which obsoleted RFC 7807 in July 2023."""
        body = {'type': 'about:blank', 'title': HTTPStatus(status).phrase,
                'status': status}
        if detail:
            body['detail'] = detail
        fields = {'Content-Type': 'application/problem+json',
                  'Cache-Control': 'no-store'}
        return status, {**fields, **(headers or {})}, body

    def query(self, sql, args=()):
        self.queries += 1
        return self.db.execute(sql, args)

    def request(self, method, target, headers=None, body=None):
        """One request, start to finish, under one lock so runs are repeatable."""
        with self.lock:
            lower = {k.lower(): v for k, v in (headers or {}).items()}
            try:
                status, fields, data = self.dispatch(method, target, lower, body)
            except (ValueError, TypeError, KeyError):
                status, fields, data = self.problem(400, 'Invalid request')
            except Exception:
                status, fields, data = self.problem(500, 'Request failed')
            if status not in (101, 204, 304):
                fields = {'Content-Type': 'application/json', **fields}
            # Method and status only: no query strings, no bodies, no tokens.
            self.metrics.append({'method': method, 'status': status})
            return status, fields, data

    # ---- routing -------------------------------------------------------

    def dispatch(self, method, target, headers, body):
        url = urlsplit(target)
        path = url.path
        query = {k: v[-1] for k, v in parse_qs(url.query).items()}
        if path == '/health':
            return 200, {}, {'status': 'ok'}
        if path == '/openapi.json':
            return 200, {}, SPEC
        if path == '/metrics':
            errors = sum(1 for m in self.metrics if m['status'] >= 500)
            return 200, {}, {'requests': len(self.metrics), 'errors': errors}
        if path == '/boom':
            raise RuntimeError('connect failed: user=api password=hunter2')
        if path == '/limited':
            return self.limited()
        if path == '/token' and method == 'POST':
            return self.mint(headers, query)
        if path == '/session':
            return self.session(method, headers)
        if path in ('/private', '/scope', '/policy'):
            return self.guarded(path, headers, query)
        if path == '/webhook' and method == 'POST':
            return self.webhook(headers, body)
        if path == '/events':
            after = int(query.get('after', '0'))
            return 200, {}, {'items': [e for e in self.events
                                       if e['id'] > after]}
        if path == '/stream':
            return self.stream(headers)
        if path == '/export':
            rows = self.query('SELECT id,title FROM tasks ORDER BY id')
            lines = ''.join(json.dumps(dict(r), separators=(',', ':')) + '\n'
                            for r in rows)
            return 200, {'Content-Type': 'application/x-ndjson'}, lines
        if path == '/socket':
            return self.handshake(headers)
        if path == '/jobs' and method == 'POST':
            job = {'id': len(self.events) + 1, 'state': 'queued'}
            self.events.append(job)
            return 202, {'Location': f"/jobs/{job['id']}"}, job
        if path.startswith('/jobs/'):
            wanted = path.rsplit('/', 1)[-1]
            job = next((e for e in self.events if str(e['id']) == wanted), None)
            return (200, {}, job) if job else self.problem(404)
        if path == '/v2/tasks':
            rows = self.query('SELECT id,title FROM tasks ORDER BY id LIMIT 2')
            return 200, {}, {'data': [dict(r) for r in rows]}
        if path == '/tasks' and method == 'OPTIONS':
            return self.preflight(headers)
        if path == '/tasks' and method in ('GET', 'HEAD'):
            return self.list_tasks(method, headers, query)
        if path == '/tasks' and method == 'POST':
            return self.create_task(headers, body)
        if path == '/tasks':
            allow = 'GET, HEAD, POST, OPTIONS'
            return self.problem(405, headers={'Allow': allow})
        if path.startswith('/tasks/'):
            return self.task(method, path, headers, body)
        return self.problem(404, 'No route matches that path')

    # ---- collection ----------------------------------------------------

    def list_tasks(self, method, headers, query):
        accept = headers.get('accept', 'application/json')
        if accept not in ('application/json', '*/*'):
            return self.problem(406, 'This resource is JSON only')
        limit = int(query.get('limit', '2'))
        if limit < 1 or limit > LIMIT_MAX:
            return self.problem(400, f'Limit must be between 1 and {LIMIT_MAX}')
        sort = query.get('sort', 'id')
        if sort not in SORTS:
            return self.problem(400, 'Unsupported sort')
        after = int(query.get('after', '0'))
        cursor = '>'
        sql = f'SELECT id,title,state,owner FROM tasks WHERE id {cursor} ?'
        args = [after]
        for field in ('state', 'owner'):
            if field in query:
                sql += f' AND {field} = ?'
                args.append(query[field])
        if 'q' in query:
            sql += ' AND title LIKE ?'
            args.append('%' + query['q'] + '%')
        sql += ' ORDER BY ' + SORTS[sort] + ' LIMIT ?'
        args.append(limit + 1)
        rows = [dict(r) for r in self.query(sql, args)]
        more = len(rows) > limit
        rows = rows[:limit]
        fields = {'Vary': 'Accept', 'Cache-Control': 'private, max-age=0'}
        if query.get('include') == 'owner':
            fields['X-Query-Count'] = str(self.embed_owners(rows))
        if 'fields' in query:
            names = query['fields'].split(',')
            if not set(names) <= FIELDS:
                return self.problem(400, 'Unsupported field')
            rows = [{k: r[k] for k in names} for r in rows]
        next_link = None
        if more and sort == 'id' and not {'state', 'owner', 'q'} & set(query):
            # This lab offers continuation for its stable identifier order only.
            next_link = f"/tasks?after={rows[-1]['id']}&limit={limit}"
        data = {'items': rows, 'next': next_link}
        # A HEAD answer keeps the headers of the GET, length included; the
        # server is what drops the body.
        return 200, fields, data

    def embed_owners(self, rows):
        """One query for every owner, not one query for every row."""
        before = self.queries
        owners = dict(self.query('SELECT id,name FROM owners'))
        for row in rows:
            row['ownerName'] = owners[row['owner']]
        return self.queries - before + 1

    def create_task(self, headers, body):
        if headers.get('content-type') != 'application/json':
            return self.problem(415, 'Send application/json')
        if not valid_new_task(body):
            return self.problem(422, 'Supply only a title of one to eighty '
                                     'characters')
        key = headers.get('idempotency-key')
        fingerprint = json.dumps(body, sort_keys=True)
        if key and key in self.replays:
            first, response = self.replays[key]
            if first != fingerprint:
                return self.problem(409, 'Key reused for another request')
            return response
        row = self.query('INSERT INTO tasks(title,state,owner) VALUES (?,?,?)',
                         (body['title'], 'open', 'alice'))
        self.db.commit()
        data = {'id': row.lastrowid, 'title': body['title'], 'state': 'open',
                'owner': 'alice'}
        response = 201, {'Location': f'/tasks/{row.lastrowid}'}, data
        if key:
            self.replays[key] = fingerprint, response
        return response

    # ---- item ----------------------------------------------------------

    def task(self, method, path, headers, body):
        parts = path.strip('/').split('/')
        row = self.query('SELECT * FROM tasks WHERE id=?',
                         (parts[1],)).fetchone()
        if row is None:
            return self.problem(404, 'No task has that identifier')
        data = dict(row)
        etag = '"' + str(data.pop('revision')) + '"'
        fields = {'ETag': etag, 'Cache-Control': 'private, max-age=0'}
        if len(parts) == 3 and parts[2] == 'owner':
            return 200, {}, {'id': data['owner']}
        if len(parts) == 3 and parts[2] == 'completion':
            if method != 'PUT':
                return self.problem(405, headers={'Allow': 'PUT'})
            self.bump(data['id'], 'UPDATE tasks SET state="done"')
            return 204, {}, None
        if method in ('GET', 'HEAD'):
            if headers.get('if-none-match') == etag:
                return 304, fields, None
            fields['Link'] = f'</tasks/{data["id"]}/owner>; rel="author"'
            return 200, fields, data
        if method == 'PATCH':
            if headers.get('if-match') != etag:
                return self.problem(412, 'Supply the current ETag in If-Match')
            if not valid_new_task(body):
                return self.problem(422, 'Supply only a title')
            self.bump(data['id'], 'UPDATE tasks SET title=?', (body['title'],))
            return 204, {}, None
        if method == 'DELETE':
            self.query('DELETE FROM tasks WHERE id=?', (data['id'],))
            self.db.commit()
            return 204, {}, None
        return self.problem(405, headers={'Allow': 'GET, HEAD, PATCH, DELETE'})

    def bump(self, task_id, sql, args=()):
        """Every write moves the revision, which is what the ETag reports."""
        self.query(sql + ', revision=revision+1 WHERE id=?',
                   (*args, task_id))
        self.db.commit()

    # ---- everything else -----------------------------------------------

    def mint(self, headers, query):
        """A lab token endpoint: credentials in, a signed token out.

        A real deployment issues tokens from an authorisation server. This is
        one route so that a lesson can hold a genuine signed token without a
        second service, and it still asks for credentials first.
        """
        if headers.get('authorization') != 'Basic YWxpY2U6ZGVtbw==':
            return self.problem(401, 'Send credentials to get a token',
                                {'WWW-Authenticate': 'Basic realm="course"'})
        claims = {'scope': query.get('scope', 'tasks:read')}
        if 'role' in query:
            claims['role'] = query['role']
        if 'sub' in query:
            claims['sub'] = query['sub']
        return 200, {'Cache-Control': 'no-store'}, {
            'token_type': 'Bearer', 'expires_in': 3600,
            'access_token': token(query.get('kid', 'current'), **claims)}

    def preflight(self, headers):
        fields = {'Allow': 'GET, HEAD, POST, OPTIONS', 'Vary': 'Origin'}
        if headers.get('origin') == 'https://course.example':
            fields.update({
                'Access-Control-Allow-Origin': headers['origin'],
                'Access-Control-Allow-Methods': 'GET, POST',
                'Access-Control-Allow-Headers': 'Content-Type, Idempotency-Key',
                'Access-Control-Max-Age': '600'})
        return 204, fields, None

    def limited(self):
        """A fixed window of two calls, so the lesson can exhaust it."""
        self.calls += 1
        if self.calls > 2:
            return self.problem(429, 'Two calls per window',
                                {'Retry-After': '1'})
        return 200, {'X-RateLimit-Limit': '2',
                     'X-RateLimit-Remaining': str(2 - self.calls)}, \
            {'remaining': 2 - self.calls}

    def session(self, method, headers):
        if method == 'POST':
            if headers.get('authorization') != 'Basic YWxpY2U6ZGVtbw==':
                return self.problem(401, 'Send credentials',
                                    {'WWW-Authenticate': 'Basic realm="course"'})
            cookie = 'session=local-demo; HttpOnly; Secure; SameSite=Lax; Path=/'
            return 201, {'Set-Cookie': cookie}, {'user': 'alice'}
        if headers.get('cookie') != 'session=local-demo':
            return self.problem(401, 'No session cookie')
        return 200, {'Cache-Control': 'no-store'}, {'user': 'alice'}

    def guarded(self, path, headers, query):
        raw = headers.get('authorization', '').removeprefix('Bearer ')
        claims = identity(raw)
        if not claims:
            return self.problem(401, 'Bearer token missing or invalid',
                                {'WWW-Authenticate': 'Bearer'})
        scopes = claims.get('scope', '').split()
        if path == '/scope' and 'tasks:write' not in scopes:
            return self.problem(403, 'Scope tasks:write is required')
        owner = query.get('owner', claims['sub'])
        if path == '/policy' and not permitted(claims, owner):
            return self.problem(403, 'The policy denied this attribute set')
        return 200, {'Cache-Control': 'no-store'}, {'user': claims['sub'],
                                                    'scope': scopes}

    def webhook(self, headers, body):
        raw = json.dumps(body, sort_keys=True, separators=(',', ':')).encode()
        expected = hmac.new(WEBHOOK_KEY, raw, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(headers.get('x-signature', ''), expected):
            return self.problem(401, 'Signature does not match the body')
        delivery = body['id']
        if delivery not in self.seen:
            self.seen.add(delivery)
            self.events.append({'id': len(self.events) + 1,
                                'delivery': delivery})
        return 202, {}, {'accepted': True, 'deliveries': len(self.seen)}

    def stream(self, headers):
        after = int(headers.get('last-event-id', '0'))
        lines = ''.join(f'id: {i}\nevent: task\ndata: {{"id":{i}}}\n\n'
                        for i in range(after + 1, 4))
        return 200, {'Content-Type': 'text/event-stream',
                     'Cache-Control': 'no-cache'}, lines

    def handshake(self, headers):
        """The upgrade handshake only: no frames are exchanged in this lab."""
        if headers.get('upgrade', '').lower() != 'websocket':
            return self.problem(426, 'Upgrade to websocket',
                                {'Upgrade': 'websocket'})
        key = headers.get('sec-websocket-key', '')
        if headers.get('sec-websocket-version') != '13':
            return self.problem(400, 'Version thirteen only')
        magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        accept = base64.b64encode(
            hashlib.sha1((key + magic).encode()).digest()).decode()
        return 101, {'Upgrade': 'websocket', 'Connection': 'Upgrade',
                     'Sec-WebSocket-Accept': accept}, None


def valid_new_task(body):
    if not isinstance(body, dict) or set(body) != {'title'}:
        return False
    return isinstance(body['title'], str) and 1 <= len(body['title']) <= 80


def permitted(claims, owner):
    """Attributes decide, not a single role name."""
    return claims.get('role') == 'admin' or claims['sub'] == owner
