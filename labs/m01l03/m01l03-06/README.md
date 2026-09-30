# m01l03-06 · Path or query string?

**Lesson:** [Headers And Content Negotiation](https://learnsome.tech/learn/apis-course/m01l03) (lesson 1.3, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can name what each header on a real response is for, negotiate a representation with Accept and read the Vary header that makes that negotiation cacheable, tell Content-Type from Accept, and decide whether a value belongs in the path or the query string.

In the lesson: Two places to put a value, and one rule that decides between them. A path segment identifies: it says which resource you are talking about, and taking it away leaves you talking about something else. A query parameter modifies: it filters, sorts, trims or pages the representation of a resource that exists either way. So an identifier and a relationship belong in the path, and a page size, a filter, a sort key and a field list belong in the query string. One thing belongs in neither: a secret. Addresses end up in logs, in browser history, in proxies and in error reports, so credentials travel in a header.

## Files

- [`starter/path-or-query-string.txt`](starter/path-or-query-string.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/path-or-query-string.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
