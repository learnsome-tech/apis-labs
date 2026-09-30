# m03l05-02 · Selection changes the representation

**Lesson:** [Partial Responses](https://learnsome.tech/learn/apis-course/m03l05) (lesson 3.5, module 3: Request And Response Design) · Pro  
**Check:** Read along

## Goal

You can design field selection and sparse representations without making hidden server calls, and keep partial responses safe, cacheable, and understandable.

In the lesson: The task still has a state and an owner even when this response selects only an identifier and a title. The resource did not change; the representation became smaller. Because the answer depends on the fields query, a shared cache must vary on that choice or it can serve the wrong shape to another caller. Links may remain when they are useful and permitted, but the rule should be consistent. A partial response is safe when its shape is explicit rather than surprising.

## Files

- [`starter/selection-changes-the-representation.txt`](starter/selection-changes-the-representation.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/selection-changes-the-representation.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
