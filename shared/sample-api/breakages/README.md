# Breakages

Numbered faults, each one patch against `app.py`, each graded by
a named class in `contract_test.py`.

| Breakage | What breaks | Lesson | Graded by |
| --- | --- | --- | --- |
| `01-missing-404` | A missing task answers two hundred with an empty body | `m01l02` | `NotFound` |
| `02-pagination-drift` | The cursor includes the row it should start after | `m03l01` | `Pagination` |
| `03-non-idempotent-retry` | A retried create makes a second task | `m04l03` | `Idempotency` |
| `04-missing-etag` | The item response carries no validator | `m01l04` | `Validators` |
| `05-leaky-500` | The five hundred body repeats the internal error | `m04l02` | `ErrorBodies` |
| `06-n-plus-one` | Embedding owners queries once per row | `m08l02` | `QueryCount` |
| `07-unbounded-list` | The page size has no ceiling | `m08l01` | `Bounds` |
| `08-unverified-jwt` | The token signature is never checked | `m05l02` | `Tokens` |

Apply with `patch -p1 < breakages/<name>/break.patch` from
`sample-api/`, revert with the same command and `-R`.
