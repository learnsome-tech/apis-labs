# m03l03-03 · Safe sort choices

**Lesson:** [Sorting Results](https://learnsome.tech/learn/apis-course/m03l03) (lesson 3.3, module 3: Request And Response Design) · Pro  
**Check:** Read along

## Goal

You can expose a safe sort vocabulary, make ordering deterministic, and explain why pagination and sorting must be designed together.

In the lesson: The service accepts a small set of names and maps them to known expressions. A leading direction marker can mean descending, but it remains data that the server interprets rather than executable syntax. An unknown key receives a bad request with a useful detail. The representation and its links keep the same shape regardless of order, so a client changes only the question it asks, not the parser it uses.

## Files

- [`starter/safe-sort-choices.txt`](starter/safe-sort-choices.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/safe-sort-choices.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
