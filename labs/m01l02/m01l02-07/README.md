# m01l02-07 · When the status lies

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: Now here is the same service with the first of the eight faults applied, and this is what a wrong status actually costs. Ask for a task that does not exist. The answer is success, and an empty object. Every client now has to guess: was the task missing, or is it real and holding nothing? Caches will store that as a valid representation. A retry loop will treat it as a result. And the bug is invisible from the outside, because nothing looks like an error. Run the contract suite over the part that covers this, and it fails, which is how you find out before your users do.

## Files

- [`starter/FAULT`](starter/FAULT)
- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-07/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/999
   python3 contract_test.py -k NotFound 2>&1 | tail -3
   ```
4. Run it: `curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3`.
5. Check it from the repository root: `./check m01l02-07`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 2
{}
Ran 2 tests in 0.515s
FAILED (failures=2)
```

## How to check

`./check m01l02-07` copies `starter/` into a scratch directory and runs `curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
