# 07-unbounded-list

**The page size has no ceiling**

Used by lesson `m08l01`. Graded by `Bounds` in `contract_test.py`.

## What goes wrong

GET /tasks?limit=100000 is answered instead of refused, so one request can ask for the whole table.

## The loop

```sh
cd sample-api
patch -p1 < breakages/07-unbounded-list/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k Bounds          # the suite fails here
patch -p1 -R < breakages/07-unbounded-list/break.patch  # put it back
python3 contract_test.py -k Bounds          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
