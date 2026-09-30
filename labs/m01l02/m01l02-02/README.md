# m01l02-02 · Create, read, update, delete, and the methods for each

**Lesson:** [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) (lesson 1.2, module 1: What An API Is And HTTP For Real) · Free  
**Check:** Read along

## Goal

You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

In the lesson: Here is the mapping people mean when they say those four operations. The collection address accepts a create. The item address, which is the collection plus an identifier, accepts a read, an update and a delete. The difference between patch and put is worth having straight: patch sends the parts you want changed, put sends the whole replacement and means everything you left out is now absent. Notice what this mapping is not. It is not a rule that every interface is four operations on a table. Plenty of real work does not fit, and lesson four of the next module is about exactly that.

## Files

- [`starter/create-read-update-delete-and-the-methods-fo.txt`](starter/create-read-update-delete-and-the-methods-fo.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/create-read-update-delete-and-the-methods-fo.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/apis-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
