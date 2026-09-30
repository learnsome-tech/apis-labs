# 05-leaky-500

**The five hundred body repeats the internal error**

Used by lesson `m04l02`. Graded by `ErrorBodies` in `contract_test.py`.

## What goes wrong

GET /boom returns the database connection string, including a password, to whoever asked.

## The loop

```sh
cd sample-api
patch -p1 < breakages/05-leaky-500/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k ErrorBodies          # the suite fails here
patch -p1 -R < breakages/05-leaky-500/break.patch  # put it back
python3 contract_test.py -k ErrorBodies          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
