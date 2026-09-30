# m01l04 · Caching And Conditional Requests

Module 1: What An API Is And HTTP For Real · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/apis-course/m01l04)

**Goal:** You can choose a cache policy, explain freshness and validation, use an ETag with conditional requests, and recognise why a missing validator wastes bandwidth and permits stale updates.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | Read the cache policy | Runs, not graded |
| [m01l04-03](m01l04-03/) | Validation saves the body | Read along |
| [m01l04-04](m01l04-04/) | Ask whether it changed | Runs, not graded |
| [m01l04-05](m01l04-05/) | The validator also protects writes | Read along |
| [m01l04-06](m01l04-06/) | A stale write loses safely | Runs, not graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Repair the missing validator

1. Apply the patch in breakages/04-missing-etag.
2. Observe the missing tag and the failed validation behaviour.
3. Restore the validator and run the contract suite.

> **Hint:** The clean task route already contains the validator logic.

## Check yourself

- What is the difference between freshness and validation?
- Why does a 304 response have no body?
- Which conditional header protects a write from a stale read?
- Why is a missing ETag a correctness problem?
- What does private cache control say about who may reuse an answer?

---

[Course README](../../README.md) · [Modern API Architecture: REST, GraphQL & gRPC on LearnSome.tech](https://learnsome.tech/courses/apis-course)
