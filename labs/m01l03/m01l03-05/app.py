# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l03 — Headers And Content Negotiation
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l03
# © LearnSome.tech
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
