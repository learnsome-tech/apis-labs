"""The contract suite: what openapi.yaml promises, checked against the server.

Run it directly and it starts its own server on a free port:

    python3 contract_test.py            all of it
    python3 contract_test.py -k etag    one concern

Every breakage in breakages/ names the test here that grades its fix, so the
loop a lesson asks for is: apply the patch, watch the wrong behaviour, repair
it, run this suite. Assertions are taken from the specification wherever the
specification says anything, so the two cannot drift apart quietly.
"""
import base64
import json
import threading
import unittest
import urllib.error
import urllib.request
import warnings

from app import LIMIT_MAX, SPEC, KEYS, sign, token
from server import serve

SERVER = None
BASE = None


def setUpModule():
    global SERVER, BASE
    warnings.simplefilter('ignore', ResourceWarning)
    SERVER = serve(0)
    BASE = f'http://127.0.0.1:{SERVER.server_port}'
    threading.Thread(target=SERVER.serve_forever, daemon=True).start()


def tearDownModule():
    SERVER.shutdown()
    SERVER.app.db.close()
    SERVER.server_close()


def call(method, path, body=None, **headers):
    """One request, returning status, headers and a decoded body."""
    data = json.dumps(body).encode() if body is not None else None
    if data is not None:
        headers.setdefault('Content-Type', 'application/json')
    request = urllib.request.Request(BASE + path, data=data, method=method,
                                     headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            raw = response.read()
            status, fields = response.status, dict(response.headers)
    except urllib.error.HTTPError as error:
        raw = error.read()
        status, fields = error.code, dict(error.headers)
        error.close()
    kind = fields.get('Content-Type', '')
    if raw and ('json' in kind):
        return status, fields, json.loads(raw)
    return status, fields, raw.decode() if raw else None


class SpecIsHonest(unittest.TestCase):
    """The specification is the source of truth, so it is read, not assumed."""

    def test_every_specified_path_answers(self):
        for path in SPEC['paths']:
            probe = path.replace('{id}', '1')
            method = 'PUT' if probe.endswith('/completion') else 'GET'
            status, _, _ = call(method, probe)
            self.assertNotEqual(status, 404, f'{probe} is specified but absent')

    def test_served_spec_matches_the_file(self):
        status, _, served = call('GET', '/openapi.json')
        self.assertEqual(status, 200)
        self.assertEqual(served['info']['version'], SPEC['info']['version'])


class NotFound(unittest.TestCase):
    """Graded fix for breakage 01."""

    def test_missing_task_is_404_with_a_problem_body(self):
        status, fields, body = call('GET', '/tasks/999')
        self.assertEqual(status, 404)
        self.assertEqual(fields['Content-Type'], 'application/problem+json')
        self.assertEqual(body['status'], 404)
        self.assertIn('404', SPEC['paths']['/tasks/{id}']['get']['responses'])

    def test_missing_task_rejects_writes_too(self):
        for method in ('PATCH', 'DELETE'):
            status, _, _ = call(method, '/tasks/999', {'title': 'x'})
            self.assertEqual(status, 404, method)


class Pagination(unittest.TestCase):
    """Graded fix for breakage 02."""

    def test_walking_every_page_sees_each_task_once(self):
        seen, path, pages = [], '/tasks?limit=2', 0
        while path and pages < 10:
            _, _, body = call('GET', path)
            seen.extend(item['id'] for item in body['items'])
            path, pages = body['next'], pages + 1
        self.assertEqual(len(seen), len(set(seen)), 'a task appeared twice')
        _, _, everything = call('GET', f'/tasks?limit={LIMIT_MAX}')
        self.assertGreaterEqual(len(seen), len(everything['items']))

    def test_the_page_shape_is_the_specified_one(self):
        _, _, body = call('GET', '/tasks')
        for key in SPEC['components']['schemas']['TaskPage']['required']:
            self.assertIn(key, body)


class Idempotency(unittest.TestCase):
    """Graded fix for breakage 03."""

    def test_replayed_key_returns_the_first_task(self):
        headers = {'Idempotency-Key': 'contract-suite-key'}
        first = call('POST', '/tasks', {'title': 'Retry me'}, **headers)
        second = call('POST', '/tasks', {'title': 'Retry me'}, **headers)
        self.assertEqual(first[0], 201)
        self.assertEqual(second[0], 201)
        self.assertEqual(first[2]['id'], second[2]['id'],
                         'the retry created a second task')

    def test_same_key_with_another_body_is_a_conflict(self):
        headers = {'Idempotency-Key': 'contract-suite-conflict'}
        call('POST', '/tasks', {'title': 'One'}, **headers)
        status, _, _ = call('POST', '/tasks', {'title': 'Two'}, **headers)
        self.assertEqual(status, 409)


class Validators(unittest.TestCase):
    """Graded fix for breakage 04."""

    def test_item_carries_an_etag_and_honours_it(self):
        status, fields, _ = call('GET', '/tasks/1')
        self.assertEqual(status, 200)
        self.assertIn('ETag', fields)
        again = call('GET', '/tasks/1', **{'If-None-Match': fields['ETag']})
        self.assertEqual(again[0], 304)

    def test_stale_validator_blocks_a_patch(self):
        _, fields, _ = call('GET', '/tasks/2')
        stale = '"0"'
        self.assertNotEqual(fields.get('ETag'), stale)
        status, _, _ = call('PATCH', '/tasks/2', {'title': 'Nope'},
                            **{'If-Match': stale})
        self.assertEqual(status, 412)


class ErrorBodies(unittest.TestCase):
    """Graded fix for breakage 05."""

    def test_a_crash_leaks_nothing(self):
        status, fields, body = call('GET', '/boom')
        self.assertEqual(status, 500)
        self.assertEqual(fields['Content-Type'], 'application/problem+json')
        text = json.dumps(body)
        for secret in ('password', 'hunter2', 'Traceback', 'sqlite'):
            self.assertNotIn(secret, text, f'the error body leaked {secret}')

    def test_problem_bodies_have_the_specified_members(self):
        _, _, body = call('GET', '/tasks/999')
        for key in SPEC['components']['schemas']['Problem']['required']:
            self.assertIn(key, body)


class QueryCount(unittest.TestCase):
    """Graded fix for breakage 06."""

    def test_embedding_owners_does_not_query_per_row(self):
        _, fields, body = call('GET', f'/tasks?limit={LIMIT_MAX}&include=owner')
        self.assertTrue(all('ownerName' in item for item in body['items']))
        self.assertLessEqual(int(fields['X-Query-Count']), 2,
                             'one query per row is the N plus one fault')


class Bounds(unittest.TestCase):
    """Graded fix for breakage 07."""

    def test_a_huge_limit_is_refused(self):
        status, _, body = call('GET', '/tasks?limit=100000')
        self.assertEqual(status, 400)
        self.assertEqual(body['status'], 400)

    def test_the_default_page_is_not_the_whole_table(self):
        _, _, body = call('GET', '/tasks')
        default = SPEC['paths']['/tasks']['get']['parameters'][0]['schema']
        self.assertLessEqual(len(body['items']), default['default'])


class Tokens(unittest.TestCase):
    """Graded fix for breakage 08."""

    def test_a_tampered_signature_is_rejected(self):
        header, payload, signature = token().split('.')
        forged = json.loads(base64.urlsafe_b64decode(payload + '==='))
        forged['sub'] = 'attacker'
        swapped = base64.urlsafe_b64encode(
            json.dumps(forged).encode()).rstrip(b'=').decode()
        tampered = f'{header}.{swapped}.{signature}'
        status, _, _ = call('GET', '/private',
                            Authorization=f'Bearer {tampered}')
        self.assertEqual(status, 401, 'an unverified signature was accepted')

    def test_a_valid_token_is_accepted_from_either_key_generation(self):
        for kid in KEYS:
            status, _, body = call('GET', '/private',
                                   Authorization=f'Bearer {token(kid)}')
            self.assertEqual(status, 200, kid)
            self.assertEqual(body['user'], 'alice')

    def test_a_signature_over_the_wrong_key_fails(self):
        header, payload, _ = token().split('.')
        wrong = sign(b'not-the-key', f'{header}.{payload}')
        status, _, _ = call('GET', '/private',
                            Authorization=f'Bearer {header}.{payload}.{wrong}')
        self.assertEqual(status, 401)

    def test_the_token_route_asks_for_credentials(self):
        status, fields, _ = call('POST', '/token')
        self.assertEqual(status, 401)
        self.assertIn('Basic', fields['WWW-Authenticate'])

    def test_a_minted_token_opens_the_guarded_route(self):
        status, _, body = call('POST', '/token',
                               Authorization='Basic YWxpY2U6ZGVtbw==')
        self.assertEqual(status, 200)
        self.assertEqual(body['token_type'], 'Bearer')
        guarded = call('GET', '/private',
                       Authorization=f"Bearer {body['access_token']}")
        self.assertEqual(guarded[0], 200)


class MethodsAndTypes(unittest.TestCase):
    """The HTTP the first module teaches, kept honest for the whole course."""

    def test_unsupported_media_type(self):
        status, _, _ = call('POST', '/tasks', None,
                            **{'Content-Type': 'text/plain'})
        self.assertEqual(status, 415)

    def test_unprocessable_body(self):
        status, _, _ = call('POST', '/tasks', {'title': ''})
        self.assertEqual(status, 422)

    def test_head_has_the_headers_and_no_body(self):
        status, fields, body = call('HEAD', '/tasks')
        self.assertEqual(status, 200)
        self.assertIn('Vary', fields)
        self.assertFalse(body)

    def test_unacceptable_media_type(self):
        status, _, _ = call('GET', '/tasks', Accept='application/xml')
        self.assertEqual(status, 406)

    def test_method_not_allowed_names_what_is_allowed(self):
        status, fields, _ = call('PUT', '/tasks', {'title': 'x'})
        self.assertEqual(status, 405)
        self.assertIn('GET', fields['Allow'])

    def test_rate_limit_arrives_with_retry_after(self):
        for _ in range(2):
            call('GET', '/limited')
        status, fields, _ = call('GET', '/limited')
        self.assertEqual(status, 429)
        self.assertEqual(fields['Retry-After'], '1')


if __name__ == '__main__':
    unittest.main(verbosity=2)
