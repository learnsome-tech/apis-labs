#!/usr/bin/env bash
# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l04 — Caching And Conditional Requests
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l04
# © LearnSome.tech
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si localhost:8765/tasks/1
