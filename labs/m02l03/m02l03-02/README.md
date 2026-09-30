# m02l03-02 · Choose a depth you can explain

**Lesson:** [Sub-resources And Relationships](https://learnsome.tech/learn/apis-course/m02l03) (lesson 2.3, module 2: REST And Resource Modelling) · Pro  
**Check:** Read along

## Goal

You can model related resources, choose between embedding and linking, and avoid paths whose depth makes ownership and change unclear.

In the lesson: One level of nesting is often enough to express a relationship. The owner of a task is easy to understand, and completion can be a resource when it has a state transition of its own. Deep paths become harder to document and harder to move when any parent changes. If a child has an independent lifecycle, give it an address that reflects that independence. The question is not how many slashes look elegant; it is whether the path tells the truth about ownership and change.

## Files

- [`starter/choose-a-depth-you-can-explain.txt`](starter/choose-a-depth-you-can-explain.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/choose-a-depth-you-can-explain.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
