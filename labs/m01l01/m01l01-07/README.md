# m01l01-07 · Ask which version you got

**Lesson:** [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) (lesson 1.1, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Graded

## Goal

You can say what an API is in terms of a contract rather than a technology, read a whole HTTP response off the screen part by part, name which version of HTTP you are speaking and why that matters, and place SOAP, GraphQL and gRPC as alternatives you will compare properly at the end of the course.

In the lesson: You do not have to guess which version you are speaking. Throw the body away, and ask the client to print the version it negotiated instead. This lab answers one point one, because the whole service is ninety lines of standard library and that is what it implements. A production service behind a modern load balancer would very likely answer two. The useful habit here is smaller than the protocol: when something about an interface surprises you, there is usually a way to ask the client what really happened rather than assuming. We will use that habit repeatedly, and it is what makes debugging an interface tractable.

## Files

- [`starter/run.sh`](starter/run.sh): the listing from the lesson
- 65 files of the course's shared working tree (`shared/sample-api/`), copied in beside the starter when the lab runs
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-07/starter`
2. Read `run.sh`.
3. The session types these commands, in order:

   ```sh
   curl -so /dev/null -w '%{http_version}\n' localhost:8765/tasks
   ```
4. Run it: `python3 server.py --port 8765 & curl -so /dev/null -w '%{http_version}\n' localhost:8765/tasks`.
5. Check it from the repository root: `./check m01l01-07`.

## Expected output

```text
1.1
```

## How to check

Before the program runs, `./check` starts it (`python3 server.py --port 8765`) and waits for port 8765, as the site does; it is stopped when the program ends.

It runs with curl 8 first on `PATH`, as on the site (the dev container has it).

`./check m01l01-07` copies `starter/` into a scratch directory and runs `python3 server.py --port 8765 & curl -so /dev/null -w '%{http_version}\n' localhost:8765/tasks` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
