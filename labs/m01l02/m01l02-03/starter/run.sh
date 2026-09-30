#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si --json '{"title":"Deploy"}' localhost:8765/tasks
curl -si localhost:8765/tasks/5
curl -siX DELETE localhost:8765/tasks/5
curl -si localhost:8765/tasks/5
