# 06-n-plus-one

**Embedding owners queries once per row**

Used by lesson `m08l02`. Graded by `QueryCount` in `contract_test.py`.

## What goes wrong

GET /tasks?include=owner reports a query count that grows with the page size instead of staying at two.

## The loop

```sh
cd sample-api
patch -p1 < breakages/06-n-plus-one/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k QueryCount          # the suite fails here
patch -p1 -R < breakages/06-n-plus-one/break.patch  # put it back
python3 contract_test.py -k QueryCount          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
