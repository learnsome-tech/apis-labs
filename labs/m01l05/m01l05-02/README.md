# m01l05-02 · Credentials in, cookie out

**Lesson:** [Cookies And CORS](https://learnsome.tech/learn/apis-course/m01l05) (lesson 1.5, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can explain a cookie backed session, choose its security attributes, read a browser preflight, and distinguish a browser origin policy from server side authentication.

In the lesson: Log in once and the service returns a created response with a session cookie. Http only keeps browser scripts from reading it, secure limits it to encrypted transport, same site limits cross site sending, and path says which addresses receive it. Send that cookie back and the service recognises the session without asking for the credentials again. Curl is doing the browser work by hand here, so you can see both directions. In a real browser the cookie jar stores the value and applies the attributes before each request.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-02/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si -u alice:demo -X POST localhost:8765/session
   curl -si -b session=local-demo localhost:8765/session
   ```
4. Run it: `curl -si -u alice:demo -X POST localhost:8765/session; curl -si -b session=local-demo localhost:8765/session`.
5. Check it from the repository root: `./check m01l05-02`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 201 Created
Content-Type: application/json
Set-Cookie: session=local-demo; HttpOnly; Secure; SameSite=Lax; Path=/
Content-Length: 16
{"user":"alice"}
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
Content-Length: 16
{"user":"alice"}
```

## How to check

`./check m01l05-02` copies `starter/` into a scratch directory and runs `curl -si -u alice:demo -X POST localhost:8765/session; curl -si -b session=local-demo localhost:8765/session` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
