#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -sI localhost:8765/tasks
curl -si localhost:8765/tasks?limit=9
