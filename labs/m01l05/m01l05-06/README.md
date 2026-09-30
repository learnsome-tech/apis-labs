# m01l05-06 · No cookie means no session

**Lesson:** [Cookies And CORS](https://learnsome.tech/learn/apis-course/m01l05) (lesson 1.5, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can explain a cookie backed session, choose its security attributes, read a browser preflight, and distinguish a browser origin policy from server side authentication.

In the lesson: Leave the cookie out and the service answers unauthorized. That is authentication doing its job. The browser policy has not changed the identity decision, and a CORS response would not make an anonymous request become a session. The no store directive is also deliberate: an authentication failure should not sit in a cache and be replayed to somebody else. When these concerns are kept separate, a client can reason about each response. One header describes browser permission, another describes identity, and the status tells you which promise failed.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-06/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/session
   ```
4. Run it: `python3 server.py --port 8765 & curl -si localhost:8765/session`.
5. Check it from the repository root: `./check m01l05-06`.

## Expected output

```text
HTTP/1.1 401 Unauthorized
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 87
{"type":"about:blank","title":"Unauthorized","status":401,"detail":"No session cookie"}
```

## How to check

Before the program runs, `./check` starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l05-06` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -si localhost:8765/session` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
