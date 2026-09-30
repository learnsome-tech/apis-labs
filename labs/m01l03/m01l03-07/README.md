# m01l03-07 · The same two headers, both directions

**Lesson:** [Headers And Content Negotiation](https://learnsome.tech/learn/apis-course/m01l03) (lesson 1.3, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can name what each header on a real response is for, negotiate a representation with Accept and read the Vary header that makes that negotiation cacheable, tell Content-Type from Accept, and decide whether a value belongs in the path or the query string.

In the lesson: Two more things worth knowing. First, you can ask for the headers on their own: the reading method that returns metadata and no body. Look at the content length. It reports the size the body would have been, not zero, because the only difference from a normal read is that the bytes are not sent. Clients use that to check whether something changed before downloading it. Second, a page size outside the range the contract allows is a bad request with a detail that names the range, and the content type of that answer is the problem format rather than plain JSON, which is a whole lesson in module four.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-07/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -sI localhost:8765/tasks
   curl -si localhost:8765/tasks?limit=9
   ```
4. Run it: `python3 server.py --port 8765 & curl -sI localhost:8765/tasks; curl -si localhost:8765/tasks?limit=9`.
5. Check it from the repository root: `./check m01l03-07`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 200 OK
Content-Type: application/json
Vary: Accept
Cache-Control: private, max-age=0
Content-Length: 154
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 98
{"type":"about:blank","title":"Bad Request","status":400,"detail":"Limit must be between 1 and 3"}
```

## How to check

`./check m01l03-07` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -sI localhost:8765/tasks; curl -si localhost:8765/tasks?limit=9` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
