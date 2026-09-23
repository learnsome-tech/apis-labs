#!/usr/bin/env bash
# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l01 — What An API Is, And The Alternatives
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l01
# © LearnSome.tech
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -so /dev/null -w '%{http_version}\n' localhost:8765/tasks
