#!/usr/bin/env bash
# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l02 — HTTP Methods And Status Codes
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l02
# © LearnSome.tech
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si localhost:8765/tasks/999
python3 contract_test.py -k NotFound 2>&1 | tail -3
