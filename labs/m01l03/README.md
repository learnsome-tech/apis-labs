# m01l03 · Headers And Content Negotiation

Module 1: What An API Is And HTTP For Real · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/apis-course/m01l03)

**Goal:** You can name what each header on a real response is for, negotiate a representation with Accept and read the Vary header that makes that negotiation cacheable, tell Content-Type from Accept, and decide whether a value belongs in the path or the query string.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | Read a real set of response headers | Runs, not graded |
| [m01l03-03](m01l03-03/) | Content negotiation, in two headers | Read along |
| [m01l03-04](m01l03-04/) | Ask for something it cannot make | Runs, not graded |
| [m01l03-05](m01l03-05/) | The negotiation, in the service | Read along |
| [m01l03-06](m01l03-06/) | Path or query string? | Read along |
| [m01l03-07](m01l03-07/) | The same two headers, both directions | Runs, not graded |

## Check yourself

- What is the difference between Accept and Content-Type?
- Why must a negotiated response carry a Vary header?
- A caller asks for XML and you have only JSON. What do you send?
- Give one value that belongs in a path segment and one that belongs in the query string.
- Why does a HEAD response report a content length that is not zero?

---

[Course README](../../README.md) · [Modern API Architecture: REST, GraphQL & gRPC on LearnSome.tech](https://learnsome.tech/courses/apis-course)
