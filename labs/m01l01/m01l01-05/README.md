# m01l01-05 · The contract, written down first

**Lesson:** [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) (lesson 1.1, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Checker

## Goal

You can say what an API is in terms of a contract rather than a technology, read a whole HTTP response off the screen part by part, name which version of HTTP you are speaking and why that matters, and place SOAP, GraphQL and gRPC as alternatives you will compare properly at the end of the course.

In the lesson: This file is the contract, and in this repository it is the source of truth. The top says what this interface is and which version of it you are looking at. Then where it can be reached. Then the operations themselves, one address at a time, each with the methods it answers and the statuses it can return. Notice the status written in quotation marks. The server reads this file when it starts, the contract suite reads it to decide what to assert, and the lessons read lines out of it onto this screen. We will write one of these properly in module six. For now, the point is that the promise exists as a document, separate from the program that keeps it.

## Files

- [`starter/SOURCE`](starter/SOURCE)
- [`starter/openapi.yaml`](starter/openapi.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `openapi.yaml` the way the lesson builds it:
   - Lines 1–5: what this interface is
   - Lines 6–8: where it can be reached
   - Lines 9–16: the operations themselves
3. Notes from the lesson:
   - Line 15: quoted, because a bare 200 in YAML would be a number, not a key
4. Edit `openapi.yaml` and check it: `yamllint openapi.yaml`.
5. Check it from the repository root: `./check m01l01-05`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m01l01-05 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed openapi.yaml`
   - `strict` (Lint strictly): `yamllint openapi.yaml`

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `yamllint openapi.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
