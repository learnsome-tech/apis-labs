<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Modern API Architecture: REST, GraphQL & gRPC

An API design course as IDE-style videos, built from one set of lesson scripts and one small service. 8 modules, 40 lessons, five to ten minutes each.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/apis-course](https://learnsome.tech/courses/apis-course)
- **Video player**: [https://learnsome.tech/courses/apis-course/watch](https://learnsome.tech/courses/apis-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/apis/book.pdf](https://learnsome.tech/handbooks/apis/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/apis-course/book](https://learnsome.tech/courses/apis-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
15 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **What An API Is And HTTP For Real** | | | |
| 1 | What An API Is, And The Alternatives | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-1-1) |
| 2 | HTTP Methods And Status Codes | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-1-2) |
| 3 | Headers And Content Negotiation | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-1-3) |
| 4 | Caching And Conditional Requests | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-1-4) |
| 5 | Cookies And CORS | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-1-5) |
| | **REST And Resource Modelling** | | | |
| 6 | The REST Constraints | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-2-1) |
| 7 | Naming Resources And Collections | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-2-2) |
| 8 | Sub-resources And Relationships | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-2-3) |
| 9 | Actions That Do Not Fit CRUD | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-2-4) |
| 10 | HATEOAS And Hypermedia | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-2-5) |
| | **Request And Response Design** | | | |
| 11 | Pagination Strategies | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-3-1) |
| 12 | Filtering And Searching | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-3-2) |
| 13 | Sorting Results | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-3-3) |
| 14 | Large Payloads And Streaming | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-3-4) |
| 15 | Partial Responses | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/apis-course/book#lesson-3-5) |
| | **Correctness Under Retry And Failure** | | | |
| 16 | Error Handling And Safe Retries | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m04l01) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-4-1) |
| 17 | Problem Details: RFC 9457 | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m04l02) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-4-2) |
| 18 | Idempotency Keys | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m04l03) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-4-3) |
| 19 | Rate Limiting Strategies | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m04l04) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-4-4) |
| 20 | Versioning APIs | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m04l05) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-4-5) |
| | **Authentication And Authorisation** | | | |
| 21 | Basic Auth, Tokens And Sessions | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m05l01) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-5-1) |
| 22 | JSON Web Tokens | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m05l02) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-5-2) |
| 23 | OAuth Two And OpenID Connect | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m05l03) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-5-3) |
| 24 | RBAC Contrasted With ABAC | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m05l04) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-5-4) |
| 25 | Scopes And Key Rotation | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m05l05) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-5-5) |
| | **Documentation And Contract** | | | |
| 26 | OpenAPI And Design-First | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m06l01) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-6-1) |
| 27 | Unit And Integration Testing | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m06l02) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-6-2) |
| 28 | Mocking Dependencies | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m06l03) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-6-3) |
| 29 | Contract Testing | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m06l04) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-6-4) |
| 30 | Load Testing | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m06l05) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-6-5) |
| | **Beyond Request And Response** | | | |
| 31 | Webhooks Versus Polling | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m07l01) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-7-1) |
| 32 | WebSockets | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m07l02) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-7-2) |
| 33 | Server-Sent Events | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m07l03) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-7-3) |
| 34 | Event-Driven Architecture And Queues | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m07l04) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-7-4) |
| 35 | API Gateways And Proxies | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m07l05) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-7-5) |
| | **Operating An API** | | | |
| 36 | Security Best Practices | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m08l01) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-8-1) |
| 37 | Performance Optimization | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m08l02) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-8-2) |
| 38 | Observability: Logs, Metrics, Traces | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m08l03) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-8-3) |
| 39 | Handling PII And Data Privacy | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m08l04) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-8-4) |
| 40 | When Each Wins: REST, GraphQL, gRPC And SOAP | [▶](https://learnsome.tech/courses/apis-course/watch?lesson=m08l05) | — | [§](https://learnsome.tech/courses/apis-course/book#lesson-8-5) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
