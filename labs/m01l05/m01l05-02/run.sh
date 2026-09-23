#!/usr/bin/env bash
# Modern API Architecture: REST, GraphQL & gRPC — lesson m01l05 — Cookies And CORS
# https://learnsome.tech/courses/apis-course/watch?lesson=m01l05
# © LearnSome.tech
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si -u alice:demo -X POST localhost:8765/session
curl -si -b session=local-demo localhost:8765/session
