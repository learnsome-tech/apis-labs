<p>
  <a href="https://learnsome.tech/courses/apis-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Modern API Architecture: REST, GraphQL & gRPC

**Contract-First Schemas, Authentication, Rate Limiting & Tracing**

An API design course as IDE-style videos, built from one set of lesson scripts and one small service. 8 modules, 40 lessons, five to ten minutes each. Intermediate level, about 2 hours.

This repository holds the labs of the LearnSome.tech course [Modern API Architecture: REST, GraphQL & gRPC](https://learnsome.tech/courses/apis-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/apis-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7 and ansible-core and yamllint, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/apis-labs.git
  cd apis-labs
  ./check m01l01-02
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7 and ansible-core and yamllint. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-02`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Checker | Validates the file with the checker the site uses (hadolint, kubeconform, actionlint, yamllint, `ansible-playbook --syntax-check` or `terraform validate`); passes when it finds no errors. | 1 |
| Runs, not graded | Runs the program and shows its output; the site gives no pass or fail, and the lab README says why. | 16 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 19 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: What An API Is And HTTP For Real

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [What An API Is, And The Alternatives](https://learnsome.tech/learn/apis-course/m01l01) | [5 labs](labs/m01l01/) | Free |
| 1.2 | [HTTP Methods And Status Codes](https://learnsome.tech/learn/apis-course/m01l02) | [6 labs](labs/m01l02/) | Free |
| 1.3 | [Headers And Content Negotiation](https://learnsome.tech/learn/apis-course/m01l03) | [6 labs](labs/m01l03/) | Free |
| 1.4 | [Caching And Conditional Requests](https://learnsome.tech/learn/apis-course/m01l04) | [5 labs](labs/m01l04/) | Free |
| 1.5 | [Cookies And CORS](https://learnsome.tech/learn/apis-course/m01l05) | [4 labs](labs/m01l05/) | Free |

### Module 2: REST And Resource Modelling

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [The REST Constraints](https://learnsome.tech/learn/apis-course/m02l01) | [1 lab](labs/m02l01/) | Pro |
| 2.2 | [Naming Resources And Collections](https://learnsome.tech/learn/apis-course/m02l02) | [1 lab](labs/m02l02/) | Pro |
| 2.3 | [Sub-resources And Relationships](https://learnsome.tech/learn/apis-course/m02l03) | [1 lab](labs/m02l03/) | Pro |
| 2.4 | [Actions That Do Not Fit CRUD](https://learnsome.tech/learn/apis-course/m02l04) | [1 lab](labs/m02l04/) | Pro |
| 2.5 | [HATEOAS And Hypermedia](https://learnsome.tech/learn/apis-course/m02l05) | [1 lab](labs/m02l05/) | Pro |

### Module 3: Request And Response Design

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Pagination Strategies](https://learnsome.tech/learn/apis-course/m03l01) | [1 lab](labs/m03l01/) | Pro |
| 3.2 | [Filtering And Searching](https://learnsome.tech/learn/apis-course/m03l02) | [1 lab](labs/m03l02/) | Pro |
| 3.3 | [Sorting Results](https://learnsome.tech/learn/apis-course/m03l03) | [1 lab](labs/m03l03/) | Pro |
| 3.4 | [Large Payloads And Streaming](https://learnsome.tech/learn/apis-course/m03l04) | [1 lab](labs/m03l04/) | Pro |
| 3.5 | [Partial Responses](https://learnsome.tech/learn/apis-course/m03l05) | [1 lab](labs/m03l05/) | Pro |

### Module 4: Correctness Under Retry And Failure

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Error Handling And Safe Retries](https://learnsome.tech/learn/apis-course/m04l01) | – | Pro |
| 4.2 | [Problem Details: RFC 9457](https://learnsome.tech/learn/apis-course/m04l02) | – | Pro |
| 4.3 | [Idempotency Keys](https://learnsome.tech/learn/apis-course/m04l03) | – | Pro |
| 4.4 | [Rate Limiting Strategies](https://learnsome.tech/learn/apis-course/m04l04) | – | Pro |
| 4.5 | [Versioning APIs](https://learnsome.tech/learn/apis-course/m04l05) | – | Pro |

### Module 5: Authentication And Authorisation

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Basic Auth, Tokens And Sessions](https://learnsome.tech/learn/apis-course/m05l01) | – | Pro |
| 5.2 | [JSON Web Tokens](https://learnsome.tech/learn/apis-course/m05l02) | – | Pro |
| 5.3 | [OAuth Two And OpenID Connect](https://learnsome.tech/learn/apis-course/m05l03) | – | Pro |
| 5.4 | [RBAC Contrasted With ABAC](https://learnsome.tech/learn/apis-course/m05l04) | – | Pro |
| 5.5 | [Scopes And Key Rotation](https://learnsome.tech/learn/apis-course/m05l05) | – | Pro |

### Module 6: Documentation And Contract

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [OpenAPI And Design-First](https://learnsome.tech/learn/apis-course/m06l01) | – | Pro |
| 6.2 | [Unit And Integration Testing](https://learnsome.tech/learn/apis-course/m06l02) | – | Pro |
| 6.3 | [Mocking Dependencies](https://learnsome.tech/learn/apis-course/m06l03) | – | Pro |
| 6.4 | [Contract Testing](https://learnsome.tech/learn/apis-course/m06l04) | – | Pro |
| 6.5 | [Load Testing](https://learnsome.tech/learn/apis-course/m06l05) | – | Pro |

### Module 7: Beyond Request And Response

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 7.1 | [Webhooks Versus Polling](https://learnsome.tech/learn/apis-course/m07l01) | – | Pro |
| 7.2 | [WebSockets](https://learnsome.tech/learn/apis-course/m07l02) | – | Pro |
| 7.3 | [Server-Sent Events](https://learnsome.tech/learn/apis-course/m07l03) | – | Pro |
| 7.4 | [Event-Driven Architecture And Queues](https://learnsome.tech/learn/apis-course/m07l04) | – | Pro |
| 7.5 | [API Gateways And Proxies](https://learnsome.tech/learn/apis-course/m07l05) | – | Pro |

### Module 8: Operating An API

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 8.1 | [Security Best Practices](https://learnsome.tech/learn/apis-course/m08l01) | – | Pro |
| 8.2 | [Performance Optimization](https://learnsome.tech/learn/apis-course/m08l02) | – | Pro |
| 8.3 | [Observability: Logs, Metrics, Traces](https://learnsome.tech/learn/apis-course/m08l03) | – | Pro |
| 8.4 | [Handling PII And Data Privacy](https://learnsome.tech/learn/apis-course/m08l04) | – | Pro |
| 8.5 | [When Each Wins: REST, GraphQL, gRPC And SOAP](https://learnsome.tech/learn/apis-course/m08l05) | – | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
