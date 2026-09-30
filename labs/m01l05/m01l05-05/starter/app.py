    def preflight(self, headers):
        fields = {'Allow': 'GET, HEAD, POST, OPTIONS', 'Vary': 'Origin'}
        if headers.get('origin') == 'https://course.example':
            fields.update({
                'Access-Control-Allow-Origin': headers['origin'],
                'Access-Control-Allow-Methods': 'GET, POST',
                'Access-Control-Allow-Headers': 'Content-Type, Idempotency-Key',
                'Access-Control-Max-Age': '600'})
        return 204, fields, None
