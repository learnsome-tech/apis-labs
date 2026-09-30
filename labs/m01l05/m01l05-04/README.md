# m01l05-04 · The browser asks before posting

**Lesson:** [Cookies And CORS](https://learnsome.tech/learn/apis-course/m01l05) (lesson 1.5, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can explain a cookie backed session, choose its security attributes, read a browser preflight, and distinguish a browser origin policy from server side authentication.

In the lesson: Before a cross origin post with a non simple request, the browser sends a preflight. It asks with options, names its origin, and names the method it plans to use. The service grants this origin permission to use get and post, permits the headers the real request needs, and says the answer may be remembered for a while. Vary origin tells shared caches that another origin might receive a different answer. The preflight has no body, so no content type or content length is needed. This is a negotiation about browser behaviour, not a login exchange.

## Files

- [`starter/preflight.py`](starter/preflight.py): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-04/starter`
2. Read `preflight.py`.
3. Run it: `python3 server.py --port 8765 & python3 preflight.py`.
4. Check it from the repository root: `./check m01l05-04`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
204
Access-Control-Allow-Origin: https://course.example
Access-Control-Allow-Methods: GET, POST
Access-Control-Max-Age: 600
```

## How to check

`./check m01l05-04` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & python3 preflight.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
