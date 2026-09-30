# m01l04-04 · Ask whether it changed

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: Send the tag back and the service confirms that nothing changed. There is no content type and no content length because there is no body. The status is not an error and it is not a redirect. It is the server saying that your stored representation remains valid. Notice that the validator comes back again. A cache can keep the metadata current even while it keeps the bytes it already owns. This is the small exchange that turns a large repeated download into a short check.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'
   ```
4. Run it: `curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'`.
5. Check it from the repository root: `./check m01l04-04`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 304 Not Modified
ETag: "1"
Cache-Control: private, max-age=0
```

## How to check

`./check m01l04-04` copies `starter/` into a scratch directory and runs `curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
