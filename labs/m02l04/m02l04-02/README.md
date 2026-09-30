# m02l04-02 · A transition can be a resource

**Lesson:** [Actions That Do Not Fit CRUD](https://learnsome.tech/learn/apis-course/m02l04) (lesson 2.4, module 2: REST And Resource Modelling) · Pro  
**Check:** Read along

## Goal

You can model an action that does not fit CRUD as a resource or state transition, choose a useful status, and make long running work observable.

In the lesson: The task completion address represents a transition whose result is the task in a done state. A put makes the request idempotent, so repeating it is harmless. A long export is different: the initial request creates a job and answers accepted because the work is not finished. The location header gives the client the job address, where it can observe progress or the final result. The status and headers together tell the client what happened and what to do next.

## Files

- [`starter/a-transition-can-be-a-resource.txt`](starter/a-transition-can-be-a-resource.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-transition-can-be-a-resource.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
