#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si -H 'Accept: application/xml' localhost:8765/tasks
curl -si -H 'Accept: */*' localhost:8765/tasks?limit=1
