#!/usr/bin/env bash
# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l03 — Headers And Content Negotiation
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l03
# © LearnSome.tech
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si -H 'Accept: application/xml' localhost:8765/tasks
curl -si -H 'Accept: */*' localhost:8765/tasks?limit=1
