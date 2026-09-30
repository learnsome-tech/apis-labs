# m01l02-06 · Three ways to be wrong, three statuses

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: Three requests that are all wrong, in three different ways, and the service distinguishes them. First, a method the collection does not take, which is method not allowed with the allow header attached. Second, a body in the wrong format entirely, which is unsupported media type: the service will not even try to read it. Third, a body in the right format saying nothing useful, which is unprocessable content: it parsed, and it still cannot be acted on. Notice how much a client learns from the difference. One says change your verb, one says change your encoding, one says change your data. A service that answered four hundred to all three would be technically defensible and useless.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -siX PUT --json '{"title":"x"}' localhost:8765/tasks
   curl -si -d 'title=x' localhost:8765/tasks
   curl -si --json '{"title":""}' localhost:8765/tasks
   ```
4. Run it: `python3 server.py --port 8765 & curl -siX PUT --json '{"title":"x"}' localhost:8765/tasks; curl -si -d 'title=x' localhost:8765/tasks; curl -si --json '{"title":""}' localhost:8765/tasks`.
5. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
HTTP/1.1 405 Method Not Allowed
Content-Type: application/problem+json
Cache-Control: no-store
Allow: GET, HEAD, POST, OPTIONS
Content-Length: 64
{"type":"about:blank","title":"Method Not Allowed","status":405}
HTTP/1.1 415 Unsupported Media Type
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 101
{"type":"about:blank","title":"Unsupported Media Type","status":415,"detail":"Send application/json"}
HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json
Cache-Control: no-store
Content-Length: 126
{"type":"about:blank","title":"Unprocessable Content","status":422,"detail":"Supply only a title of one to eighty characters"}
```

## How to check

Before the program runs, `./check` starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l02-06` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -siX PUT --json '{"title":"x"}' localhost:8765/tasks; curl -si -d 'title=x' localhost:8765/tasks; curl -si --json '{"title":""}' localhost:8765/tasks` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
