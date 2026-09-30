# m01l03-02 · Read a real set of response headers

**Lesson:** [Headers And Content Negotiation](https://learnsome.tech/learn/apis-course/m01l03) (lesson 1.3, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can name what each header on a real response is for, negotiate a representation with Accept and read the Vary header that makes that negotiation cacheable, tell Content-Type from Accept, and decide whether a value belongs in the path or the query string.

In the lesson: Ask for one page of the collection and read the headers rather than the body. Content type names the format, so the caller knows how to parse what follows. Content length says how many bytes to expect, which is how the client knows the message ended. Cache control says how this answer may be stored, and we take that apart in the next lesson. And vary names the request headers that changed this answer, which is the header most people have never used and which makes the whole idea of negotiation safe. Four headers, and three of them are instructions to machinery you did not write.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-02/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks?limit=1
   ```
4. Run it: `curl -si localhost:8765/tasks?limit=1`.
5. Check it from the repository root: `./check m01l03-02`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 200 OK
Content-Type: application/json
Vary: Accept
Cache-Control: private, max-age=0
Content-Length: 100
{"items":[{"id":1,"title":"Design","state":"open","owner":"alice"}],"next":"/tasks?after=1&limit=1"}
```

## How to check

`./check m01l03-02` copies `starter/` into a scratch directory and runs `curl -si localhost:8765/tasks?limit=1` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
