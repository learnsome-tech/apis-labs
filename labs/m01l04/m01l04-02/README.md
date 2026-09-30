# m01l04-02 · Read the cache policy

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: Read one task and look at the metadata before the body. This service permits a private cache to keep the answer, but its maximum age is zero, so the cache must validate it before reuse. The ETag is the validator. Think of it as a name for this exact representation. The link header is unrelated to caching, but it is a useful reminder that headers can carry several independent instructions beside the body. A policy is only helpful when the representation has a stable identity to validate, which is why the tag and the cache rule appear together here.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/1
   ```
4. Run it: `curl -si localhost:8765/tasks/1`.
5. Check it from the repository root: `./check m01l04-02`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 200 OK
Content-Type: application/json
ETag: "1"
Cache-Control: private, max-age=0
Link: </tasks/1/owner>; rel="author"
Content-Length: 56
{"id":1,"title":"Design","state":"open","owner":"alice"}
```

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `curl -si localhost:8765/tasks/1` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
