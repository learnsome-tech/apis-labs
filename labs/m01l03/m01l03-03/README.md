# m01l03-03 · Content negotiation, in two headers

**Lesson:** [Headers And Content Negotiation](https://learnsome.tech/learn/apis-course/m01l03) (lesson 1.3, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can name what each header on a real response is for, negotiate a representation with Accept and read the Vary header that makes that negotiation cacheable, tell Content-Type from Accept, and decide whether a value belongs in the path or the query string.

In the lesson: Negotiation is the mechanism by which two parties agree on a format without either of them hard coding it. The caller sends accept, which is a wish list and may carry preferences. Whoever sends a body sends content type, which is a statement about the bytes actually present. If nothing on the wish list can be produced, the honest answer is not acceptable rather than sending something else and hoping. And because the answer now depends on a request header, the server must say so with vary, or a cache will happily serve the wrong format to the next caller. The same mechanism covers language and compression, with different header names and identical logic.

## Files

- [`starter/content-negotiation-in-two-headers.txt`](starter/content-negotiation-in-two-headers.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/content-negotiation-in-two-headers.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
