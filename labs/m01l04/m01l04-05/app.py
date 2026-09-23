# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l04 — Caching And Conditional Requests
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l04
# © LearnSome.tech
        if method in ('GET', 'HEAD'):
            if headers.get('if-none-match') == etag:
                return 304, fields, None
            fields['Link'] = f'</tasks/{data["id"]}/owner>; rel="author"'
            return 200, fields, data
        if method == 'PATCH':
            if headers.get('if-match') != etag:
                return self.problem(412, 'Supply the current ETag in If-Match')
