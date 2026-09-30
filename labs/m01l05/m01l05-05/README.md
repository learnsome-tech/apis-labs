# m01l05-05 · The preflight decision

**Lesson:** [Cookies And CORS](https://learnsome.tech/learn/apis-course/m01l05) (lesson 1.5, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can explain a cookie backed session, choose its security attributes, read a browser preflight, and distinguish a browser origin policy from server side authentication.

In the lesson: The preflight handler starts with the general method list and the vary warning. It only adds permission when the origin is one the service recognises. The allowed origin is copied into the response, which avoids accidentally granting every site. Then the service names the methods and headers the browser may use, and gives the browser a time to remember this decision. This is deliberately explicit. A wildcard can be convenient for public data, but it is a dangerous answer beside credentials, and it gives a caller less control over who may read a response.

## Files

- [`starter/SOURCE`](starter/SOURCE)
- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: general method list
   - Lines 3–4: the allowed origin
   - Lines 5–9: permission
3. Notes from the lesson:
   - Line 2: Vary prevents one origin's permission being reused for another

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
