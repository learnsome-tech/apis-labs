# m01l04-03 · Validation saves the body

**Lesson:** [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) (lesson 1.4, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

In the lesson: Validation is the cheaper form of a cache hit. The client sends the tag it already has in an if none match header. If the server agrees that the representation is unchanged, it answers not modified and sends no body. The client keeps its stored bytes and updates any metadata it needs. If the tag no longer matches, the server sends the new representation with a normal success status. This still costs a round trip, but it avoids transferring the body, which is especially valuable when the answer is large or the caller is far away.

## Files

- [`starter/validation-saves-the-body.txt`](starter/validation-saves-the-body.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/validation-saves-the-body.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
