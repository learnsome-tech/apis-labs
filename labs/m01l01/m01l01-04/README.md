# m01l01-04 · A resource, as data

**Lesson:** [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) (lesson 1.1, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Runs, not graded

## Goal

You can say what an API is in terms of a contract rather than a technology, read a whole HTTP response off the screen part by part, name which version of HTTP you are speaking and why that matters, and place SOAP, GraphQL and gRPC as alternatives you will compare properly at the end of the course.

In the lesson: The service holds tasks. Ask for two of them, and pipe the answer through a formatter so it is readable on screen. What comes back is a page: a list of items, and a link to the page after this one. Every item has an identifier, a title, a state and an owner. This is what people mean by a representation. The task is not this text; the task lives in a database. This is one rendering of it, in one format, chosen because we asked for it. Hold on to that distinction, because in module two the difference between a resource and its representation is what makes the design decisions make sense.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-04/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -s localhost:8765/tasks?limit=2 | python3 -m json.tool
   ```
4. Run it: `python3 server.py --port 8765 & curl -s localhost:8765/tasks?limit=2 | python3 -m json.tool`.
5. Check it from the repository root: `./check m01l01-04`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
{
    "items": [
        {
            "id": 1,
            "title": "Design",
            "state": "open",
            "owner": "alice"
        },
        {
            "id": 2,
            "title": "Build",
            "state": "open",
            "owner": "bob"
        }
    ],
    "next": "/tasks?after=2&limit=2"
}
```

## How to check

`./check m01l01-04` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -s localhost:8765/tasks?limit=2 | python3 -m json.tool` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
