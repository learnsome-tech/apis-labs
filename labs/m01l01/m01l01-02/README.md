# m01l01-02 · The smallest exchange there is

**Lesson:** [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) (lesson 1.1, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can say what an API is in terms of a contract rather than a technology, read a whole HTTP response off the screen part by part, name which version of HTTP you are speaking and why that matters, and place SOAP, GraphQL and gRPC as alternatives you will compare properly at the end of the course.

In the lesson: The service this course builds is running on your own machine. Ask it whether it is alive, and read the answer from the top. The first line is the version and the status. Then the headers, which are the metadata about the answer. Then a blank line, and then the body. Now ask it for an address it does not have. Same shape, different status, and a body that describes the problem rather than the resource. Those two exchanges already contain the whole vocabulary: a status, some headers, a body. For the rest of this module we are going to look at each of those parts closely, because nearly every design decision in an interface is taken in one of them.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-02/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/health
   curl -si localhost:8765/nope
   ```
4. Run it: `curl -si localhost:8765/health; curl -si localhost:8765/nope`.
5. Check it from the repository root: `./check m01l01-02`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 15
{"status":"ok"}
HTTP/1.1 404 Not Found
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 93
{"type":"about:blank","title":"Not Found","status":404,"detail":"No route matches that path"}
```

## How to check

`./check m01l01-02` copies `starter/` into a scratch directory and runs `curl -si localhost:8765/health; curl -si localhost:8765/nope` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
