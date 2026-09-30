# m02l01-04 · Inspect the same interface

**Lesson:** [The REST Constraints](https://learnsome.tech/learn/apis-course/m02l01) (lesson 2.1, module 2: REST And Resource Modelling) · Pro  
**Check:** Read along

## Goal

You can explain the REST constraints, distinguish a resource from a route, and judge a simple JSON API by the uniform interface it gives every client.

In the lesson: Look at four requests to the task service. A collection and an identified item use the same method vocabulary, while the address tells you which resource is involved. The method supplies the intent, and the response still follows the HTTP shape from module one. Nothing here exposes the table name, a join, or a database transaction. That separation is the value of resource modelling: the public interface can remain stable while the implementation changes underneath it. The next lessons make the names and relationships precise.

## Files

- [`starter/inspect-the-same-interface.txt`](starter/inspect-the-same-interface.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/inspect-the-same-interface.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
