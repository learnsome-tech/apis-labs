#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -siX PUT --json '{"title":"x"}' localhost:8765/tasks
curl -si -d 'title=x' localhost:8765/tasks
curl -si --json '{"title":""}' localhost:8765/tasks
