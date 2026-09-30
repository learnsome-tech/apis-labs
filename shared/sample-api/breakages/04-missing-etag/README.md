# 04-missing-etag

**The item response carries no validator**

Used by lesson `m01l04`. Graded by `Validators` in `contract_test.py`.

## What goes wrong

GET /tasks/1 has no ETag, so no client can make a conditional request and every refetch is a full body.

## The loop

```sh
cd sample-api
patch -p1 < breakages/04-missing-etag/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k Validators          # the suite fails here
patch -p1 -R < breakages/04-missing-etag/break.patch  # put it back
python3 contract_test.py -k Validators          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
