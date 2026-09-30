# 02-pagination-drift

**The cursor includes the row it should start after**

Used by lesson `m03l01`. Graded by `Pagination` in `contract_test.py`.

## What goes wrong

Walking the pages shows the last task of one page again as the first task of the next.

## The loop

```sh
cd sample-api
patch -p1 < breakages/02-pagination-drift/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k Pagination          # the suite fails here
patch -p1 -R < breakages/02-pagination-drift/break.patch  # put it back
python3 contract_test.py -k Pagination          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
