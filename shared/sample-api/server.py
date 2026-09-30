"""Bind the task API to loopback. Run: python3 server.py --port 8765

Loopback only, on purpose: nothing in this course asks a learner to expose a
teaching service. `serve(port=0)` picks a free port, which is how the contract
suite and the course verifier run several servers at once.
"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from app import App

MAX_BODY = 16384


def serve(port=0):
    app = App()

    class Handler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'
        server_version = 'CourseTasks/1.2'

        def version_string(self):
            return self.server_version

        def log_message(self, *_args):
            pass

        def handle_request(self):
            size = int(self.headers.get('Content-Length', '0'))
            if size > MAX_BODY:
                status, fields, data = app.problem(413, 'Body too large')
                self.close_connection = True
            else:
                raw = self.rfile.read(size)
                kind = self.headers.get('Content-Type', '')
                try:
                    # A body in another media type reaches the router intact,
                    # so the router is the one that answers 415.
                    body = json.loads(raw) if raw and 'json' in kind else \
                        (raw.decode(errors='replace') or None)
                    status, fields, data = app.request(
                        self.command, self.path, dict(self.headers), body)
                except ValueError:
                    status, fields, data = app.problem(400, 'Body is not JSON')
            self.reply(status, fields, data)

        def reply(self, status, fields, data):
            if data is None:
                raw = b''
            elif isinstance(data, str):
                raw = data.encode()
            else:
                raw = json.dumps(data, separators=(',', ':')).encode()
            self.send_response(status)
            for key, value in fields.items():
                self.send_header(key, value)
            bodiless = status in (101, 204, 304)
            if not bodiless:
                self.send_header('Content-Length', str(len(raw)))
            self.end_headers()
            if not bodiless and self.command != 'HEAD':
                self.wfile.write(raw)
            if status == 101:
                # Handshake lab only: there is no frame loop behind this.
                self.close_connection = True

        do_GET = do_HEAD = do_POST = do_PUT = handle_request
        do_PATCH = do_DELETE = do_OPTIONS = handle_request

    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.app = app
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    running = serve(args.port)
    print(f'Listening on http://127.0.0.1:{running.server_port}', flush=True)
    running.serve_forever()
