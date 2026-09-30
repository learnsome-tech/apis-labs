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
