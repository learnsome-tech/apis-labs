# m01l02-04 · Where the method decision is taken

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: This is the item route in the service, and it is one decision per method. The reading methods come first, and they can answer either two hundred or three oh four, which is the next lesson but one. The update checks a precondition, then the body, then writes. The delete removes the row and answers with no content. And the last line is the one people forget: if the method was none of those, the answer is method not allowed, and it must say what it will accept. A client that gets a bare rejection has to guess; a client that gets the allow header knows.

## Files

- [`starter/SOURCE`](starter/SOURCE)
- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: the reading methods
   - Lines 6–12: the update
   - Lines 13–16: the delete
   - Lines 17: the last line
3. Notes from the lesson:
   - Line 17: 405 must say which methods are allowed, in the Allow header

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
