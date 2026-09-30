"""Run a .http request file against the service, and check its expectations.

    python3 tools/http_run.py requests/m01l02.http
    BASE_URL=http://127.0.0.1:9000 python3 tools/http_run.py requests/*.http

File format, which is the one editors already understand, plus one comment that
this runner treats as an assertion:

    ### a name for this request
    # expect 200
    GET {{base}}/tasks?limit=2
    Accept: application/json

    {"title": "a JSON body goes after a blank line"}

Every request prints one TAP style line, `ok` or `not ok`, and the process exits
non-zero if anything was not what the file expected. Captured values can be fed
forward: `# capture etag = header ETag` then `If-Match: {{etag}}`.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = os.environ.get('BASE_URL', 'http://127.0.0.1:8765')


def parse(text):
    """Requests, in file order."""
    requests = []
    current = None
    for line in text.split('\n'):
        if line.startswith('###'):
            current = {'name': line[3:].strip() or 'request', 'expect': None,
                       'method': None, 'url': None, 'headers': {},
                       'body': [], 'captures': [], 'in_body': False}
            requests.append(current)
            continue
        if current is None:
            continue
        if line.startswith('# expect'):
            current['expect'] = int(line.split()[-1])
            continue
        if line.startswith('# capture'):
            name, source = line[len('# capture'):].split('=')
            current['captures'].append((name.strip(), source.strip().split()))
            continue
        if line.startswith('#'):
            continue
        if current['method'] is None:
            if line.strip():
                current['method'], current['url'] = line.split(None, 1)
            continue
        if not current['in_body']:
            if line.strip() == '':
                current['in_body'] = True
                continue
            key, value = line.split(':', 1)
            current['headers'][key.strip()] = value.strip()
            continue
        current['body'].append(line)
    return requests


def fill(text, values):
    text = text.replace('{{base}}', BASE)
    for key, value in values.items():
        text = text.replace('{{' + key + '}}', str(value))
    return text


def send(request, values):
    url = fill(request['url'].strip(), values)
    headers = {k: fill(v, values) for k, v in request['headers'].items()}
    body = fill('\n'.join(request['body']).strip(), values)
    data = body.encode() if body else None
    call = urllib.request.Request(url, data=data, method=request['method'],
                                  headers=headers)
    try:
        with urllib.request.urlopen(call) as response:
            return response.status, dict(response.headers), response.read()
    except urllib.error.HTTPError as error:
        raw = error.read()
        status, fields = error.code, dict(error.headers)
        error.close()
        return status, fields, raw


def capture(request, status, fields, raw, values):
    for name, source in request['captures']:
        if source[0] == 'header':
            values[name] = fields.get(source[1], '')
        elif source[0] == 'status':
            values[name] = status
        elif source[0] == 'json':
            document = json.loads(raw or b'{}')
            for key in re.findall(r'[^.\[\]]+', source[1]):
                if isinstance(document, list) and key.isdigit():
                    document = document[int(key)]
                elif isinstance(document, dict) and key in document:
                    document = document[key]
                else:
                    # The assertion below is what reports this properly.
                    document = ''
                    break
            values[name] = document


def main(paths):
    values = {}
    failures = 0
    for path in paths:
        for request in parse(open(path).read()):
            status, fields, raw = send(request, values)
            capture(request, status, fields, raw, values)
            expected = request['expect']
            ok = expected is None or expected == status
            failures += 0 if ok else 1
            mark = 'ok' if ok else 'not ok'
            wanted = '' if expected is None else f' (expected {expected})'
            print(f"{mark} {status} {request['method']} {request['name']}"
                  f"{'' if ok else wanted}")
    print(f'{len(paths)} file(s), {failures} failure(s)')
    return 1 if failures else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1:]))
