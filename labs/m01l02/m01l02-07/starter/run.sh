#!/usr/bin/env bash
# The session from the video, as a script you can run.
# Start the API first:  cd sample-api && python3 server.py --port 8765
set -u

curl -si localhost:8765/tasks/999
python3 contract_test.py -k NotFound 2>&1 | tail -3
