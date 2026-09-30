# m01l01-03 · The parts of a request and a response

**Lesson:** [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) (lesson 1.1, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can say what an API is in terms of a contract rather than a technology, read a whole HTTP response off the screen part by part, name which version of HTTP you are speaking and why that matters, and place SOAP, GraphQL and gRPC as alternatives you will compare properly at the end of the course.

In the lesson: Here is the shape written out. A request begins with a method, then the target it is aimed at, then the protocol version. Under that come headers, one per line. Then a blank line, then the body, if there is one. A response is the same idea the other way round: version, status code, status phrase, then headers, then a blank line, then the body. Notice that both directions are just text. You can type a request by hand and you can read a response with your eyes, and that transparency is the reason this protocol won. It also means every disagreement between two services is visible if you are willing to look at the bytes.

## Files

- [`starter/the-parts-of-a-request-and-a-response.txt`](starter/the-parts-of-a-request-and-a-response.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-parts-of-a-request-and-a-response.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
