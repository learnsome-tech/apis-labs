# m03l02-03 · Compose filters deliberately

**Lesson:** [Filtering And Searching](https://learnsome.tech/learn/apis-course/m03l02) (lesson 3.2, module 3: Request And Response Design) · Pro  
**Check:** Read along

## Goal

You can design filter parameters, distinguish exact filtering from text search, validate unsupported values, and keep filtered pages predictable.

In the lesson: The lab combines exact filters for state and owner, and it combines a text query with a page limit. Multiple exact filters normally narrow the result together. Whatever combination the caller chooses, the response keeps the same page shape so a client does not need a special parser. If another page exists, its next link must preserve every filter and search term. Losing one parameter in the continuation is a form of pagination drift that only appears after the first page.

## Files

- [`starter/compose-filters-deliberately.txt`](starter/compose-filters-deliberately.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/compose-filters-deliberately.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
