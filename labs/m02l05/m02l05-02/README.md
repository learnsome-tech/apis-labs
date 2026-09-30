# m02l05-02 · Links reduce guessed addresses

**Lesson:** [HATEOAS And Hypermedia](https://learnsome.tech/learn/apis-course/m02l05) (lesson 2.5, module 2: REST And Resource Modelling) · Pro  
**Check:** Read along

## Goal

You can use links as part of a representation, explain how hypermedia reduces client coupling, and distinguish a server supplied link from a guessed URI.

In the lesson: The task response carries an author link, and the collection carries a next link. Each target is paired with a relation that explains its meaning. A client does not need to know whether the service uses a slash, a version prefix, or a cursor token in the next address. It follows what the server supplied. That reduces coupling and lets the server change its internal routing while preserving the relationship names that clients understand.

## Files

- [`starter/links-reduce-guessed-addresses.txt`](starter/links-reduce-guessed-addresses.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/links-reduce-guessed-addresses.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
