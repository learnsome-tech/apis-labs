# m01l02-07 · When the status lies

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: Now here is the same service with the first of the eight faults applied, and this is what a wrong status actually costs. Ask for a task that does not exist. The answer is success, and an empty object. Every client now has to guess: was the task missing, or is it real and holding nothing? Caches will store that as a valid representation. A retry loop will treat it as a result. And the bug is invisible from the outside, because nothing looks like an error. Run the contract suite over the part that covers this, and it fails, which is how you find out before your users do.

## Files

- [`starter/FAULT`](starter/FAULT)
- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-07/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/999
   python3 contract_test.py -k NotFound 2>&1 | tail -3
   ```
4. Run it: `python3 server.py --port 8765 & curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3`.
5. Check it from the repository root: `./check m01l02-07`.

## Expected output

```text
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 2
{}
Ran 2 tests in 0.515s
FAILED (failures=2)
```

## How to check

Before the program runs, `./check` applies the lab's fault (`breakages/01-missing-404/break.patch`) to the course's sample API, then starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l02-07` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -si localhost:8765/tasks/999; python3 contract_test.py -k NotFound 2>&1 | tail -3` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
