#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -so /dev/null -w '%{http_version}\n' localhost:8765/tasks
