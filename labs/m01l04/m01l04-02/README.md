# m01l04-02 · Read the cache policy

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: Read one task and look at the metadata before the body. This service permits a private cache to keep the answer, but its maximum age is zero, so the cache must validate it before reuse. The ETag is the validator. Think of it as a name for this exact representation. The link header is unrelated to caching, but it is a useful reminder that headers can carry several independent instructions beside the body. A policy is only helpful when the representation has a stable identity to validate, which is why the tag and the cache rule appear together here.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/1
   ```
4. Run it: `python3 server.py --port 8765 & curl -si localhost:8765/tasks/1`.
5. Check it from the repository root: `./check m01l04-02`.

## Expected output

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

Before the program runs, `./check` starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l04-02` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -si localhost:8765/tasks/1` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
