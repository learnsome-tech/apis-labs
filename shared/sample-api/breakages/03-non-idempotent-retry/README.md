# 03-non-idempotent-retry

**A retried create makes a second task**

Used by lesson `m04l03`. Graded by `Idempotency` in `contract_test.py`.

## What goes wrong

The same Idempotency-Key twice returns two different identifiers, so a timed out client that retries is charged twice.

## The loop

```sh
cd sample-api
patch -p1 < breakages/03-non-idempotent-retry/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k Idempotency          # the suite fails here
patch -p1 -R < breakages/03-non-idempotent-retry/break.patch  # put it back
python3 contract_test.py -k Idempotency          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
