# m02l02-02 · Path segments identify

**Lesson:** [Naming Resources And Collections](https://learnsome.tech/learn/apis-course/m02l02) (lesson 2.2, module 2: REST And Resource Modelling) · Pro  
**Check:** Read along

## Goal

You can name collections and items consistently, choose path segments for identity, and reject verbs, case surprises, and database names in public URIs.

In the lesson: These three addresses show the hierarchy without putting an action in the path. The collection is a set, the item is one member, and owner is a related resource beneath that item. The method still says whether the caller is reading, changing, or deleting. A path segment belongs here when removing it changes which resource the message is about. Filters and page controls are different; they shape a representation and belong in the query string.

## Files

- [`starter/path-segments-identify.txt`](starter/path-segments-identify.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/path-segments-identify.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
