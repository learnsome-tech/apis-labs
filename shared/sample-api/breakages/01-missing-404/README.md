# 01-missing-404

**A missing task answers two hundred with an empty body**

Used by lesson `m01l02`. Graded by `NotFound` in `contract_test.py`.

## What goes wrong

GET /tasks/999 returns 200 and {} instead of a 404 problem document, so a client cannot tell absent from empty.

## The loop

```sh
cd sample-api
patch -p1 < breakages/01-missing-404/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k NotFound          # the suite fails here
patch -p1 -R < breakages/01-missing-404/break.patch  # put it back
python3 contract_test.py -k NotFound          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
