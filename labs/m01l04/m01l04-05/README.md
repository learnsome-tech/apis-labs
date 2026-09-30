# m01l04-05 · The validator also protects writes

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: The same idea protects an update from overwriting somebody else. A get checks if none match because the caller wants to know whether its copy is still useful. A patch checks if match because the caller wants permission to change the version it read. If the tags differ, the server answers precondition failed and leaves the task alone. That is optimistic concurrency: read a version, prepare a change, and make the write conditional on that version still being current. Caching and correctness look like separate topics until you notice that both depend on naming a representation precisely.

## Files

- [`starter/SOURCE`](starter/SOURCE)
- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: if none match
   - Lines 4–6: representation
   - Lines 7–8: conditional
3. Notes from the lesson:
   - Line 8: If-Match makes an update conditional on the version read

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
