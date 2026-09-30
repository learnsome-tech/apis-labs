# m01l02 · HTTP Methods And Status Codes

Module 1: What An API Is And HTTP For Real · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/apis-course/m01l02)

**Goal:** You can choose the method that matches what a request really does, say which methods are safe and which are idempotent, read a status code as a family and then as a specific promise, and recognise the damage done by a service that answers the wrong status.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | Create, read, update, delete, and the methods for each | Read along |
| [m01l02-03](m01l02-03/) | A create, a read, and a delete | Runs, not graded |
| [m01l02-04](m01l02-04/) | Where the method decision is taken | Read along |
| [m01l02-06](m01l02-06/) | Three ways to be wrong, three statuses | Runs, not graded |
| [m01l02-07](m01l02-07/) | When the status lies | Runs, not graded |
| [m01l02-08](m01l02-08/) | The fix, and who says it is fixed | Runs, not graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break it, then fix it yourself

1. Apply the fault: patch -p1 < breakages/01-missing-404/break.patch
2. Restart the server and confirm that GET /tasks/999 answers 200 with {}
3. Repair app.py by hand so a missing task is a 404 problem document
4. Grade it: python3 contract_test.py -k NotFound

> **Hint:** The route reads the row first. The only question is what it returns when there is no row.

## Check yourself

- Which two promises does a method carry, and which methods make each?
- What must a four zero five response include, and why?
- A body arrives that parses but makes no sense. Which status, and why not the other one?
- Why is an empty success worse than a not found for a missing resource?
- What does a create response owe the client besides the created status?

---

[Course README](../../README.md) · [Modern API Architecture: REST, GraphQL & gRPC on LearnSome.tech](https://learnsome.tech/courses/apis-course)
