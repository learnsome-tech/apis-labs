# m01l02-08 · The fix, and who says it is fixed

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: The faults in this course are patches against one file, and this is how the fault is applied and taken away again. This run is a rehearsal, so nothing is changed on disk. Then the correct answer, from the repaired service: not found, a problem document, and a detail line that tells a person what went wrong. Then the same two tests, passing. That loop is the whole shape of this course. Apply a numbered fault. Watch the wrong behaviour with your own eyes. Repair it. Let the suite say whether your repair is right, rather than trusting your own reading of your own code.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-08/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   patch -p1 --dry-run < breakages/01-missing-404/break.patch
   curl -si localhost:8765/tasks/999
   python3 contract_test.py -k NotFound 2>&1 | tail -3
   ```
4. Run it: `python3 server.py --port 8765 & patch -p1 --dry-run < breakages/01-missing-404/break.patch; curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3`.
5. Check it from the repository root: `./check m01l02-08`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
checking file app.py
HTTP/1.1 404 Not Found
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 94
{"type":"about:blank","title":"Not Found","status":404,"detail":"No task has that identifier"}
Ran 2 tests in 0.514s
OK
```

## How to check

`./check m01l02-08` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & patch -p1 --dry-run < breakages/01-missing-404/break.patch; curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
