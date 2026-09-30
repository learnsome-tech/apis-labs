# m01l02-03 · A create, a read, and a delete

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: Watch a whole life in four commands. Create one task, and look at what a create owes you: the created status, and a location header saying where the new thing lives. Read it back from that address. Then delete it, which answers with the status that means done, nothing to say, no body at all. Then ask for it again, and you get the not found status with a problem document. Four requests, four different statuses, and each status was chosen rather than defaulted. Notice that the delete response has no content type either, because there is nothing to describe.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si --json '{"title":"Deploy"}' localhost:8765/tasks
   curl -si localhost:8765/tasks/5
   curl -siX DELETE localhost:8765/tasks/5
   curl -si localhost:8765/tasks/5
   ```
4. Run it: `python3 server.py --port 8765 & curl -si --json '{"title":"Deploy"}' localhost:8765/tasks; curl -si localhost:8765/tasks/5; curl -siX DELETE localhost:8765/tasks/5; curl -si localhost:8765/tasks/5`.
5. Check it from the repository root: `./check m01l02-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 201 Created
Content-Type: application/json
Location: /tasks/5
Content-Length: 56
{"id":5,"title":"Deploy","state":"open","owner":"alice"}
HTTP/1.1 200 OK
Content-Type: application/json
ETag: "1"
Cache-Control: private, max-age=0
Link: </tasks/5/owner>; rel="author"
Content-Length: 56
{"id":5,"title":"Deploy","state":"open","owner":"alice"}
HTTP/1.1 204 No Content
HTTP/1.1 404 Not Found
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 94
{"type":"about:blank","title":"Not Found","status":404,"detail":"No task has that identifier"}
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -si --json '{"title":"Deploy"}' localhost:8765/tasks; curl -si localhost:8765/tasks/5; curl -siX DELETE localhost:8765/tasks/5; curl -si localhost:8765/tasks/5` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
