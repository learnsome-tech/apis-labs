# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l05 — Cookies And CORS
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l05
# © LearnSome.tech
import os
import urllib.request
base = os.environ['BASE_URL']
headers = {'Origin': 'https://course.example',
           'Access-Control-Request-Method': 'POST'}
request = urllib.request.Request(base + '/tasks', method='OPTIONS',
                                 headers=headers)
with urllib.request.urlopen(request) as response:
    print(response.status)
    for key in ('Access-Control-Allow-Origin',
                'Access-Control-Allow-Methods',
                'Access-Control-Max-Age'):
        print(key + ': ' + response.headers[key])
