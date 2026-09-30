# m03l01-02 · Offset pagination is easy to read

**Lesson:** [Pagination Strategies](https://learnsome.tech/learn/apis-course/m03l01) (lesson 3.1, module 3: Request And Response Design) · Pro  
**Check:** Read along

## Goal

You can choose offset or cursor pagination, return stable page metadata, and prevent duplicates and gaps when a collection changes while a client walks it.

In the lesson: Offset pagination names a page by how many rows come before it. It is easy to explain and useful for small, mostly stable collections. Its weakness appears when rows are inserted or removed while a client is walking. The same row can move to a later page, or a row can be skipped entirely. Large offsets can also make a database scan work through every skipped row. Offset is a tool, not a default that fits every workload.

## Files

- [`starter/offset-pagination-is-easy-to-read.txt`](starter/offset-pagination-is-easy-to-read.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/offset-pagination-is-easy-to-read.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
