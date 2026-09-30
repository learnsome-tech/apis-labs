# m01l04-04 · Ask whether it changed

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: Send the tag back and the service confirms that nothing changed. There is no content type and no content length because there is no body. The status is not an error and it is not a redirect. It is the server saying that your stored representation remains valid. Notice that the validator comes back again. A cache can keep the metadata current even while it keeps the bytes it already owns. This is the small exchange that turns a large repeated download into a short check.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'
   ```
4. Run it: `python3 server.py --port 8765 & curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'`.
5. Check it from the repository root: `./check m01l04-04`.

## Expected output

```text
HTTP/1.1 304 Not Modified
ETag: "1"
Cache-Control: private, max-age=0
```

## How to check

Before the program runs, `./check` starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l04-04` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -si localhost:8765/tasks/1 -H 'If-None-Match: "1"'` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
