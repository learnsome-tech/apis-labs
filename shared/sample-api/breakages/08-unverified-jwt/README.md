# 08-unverified-jwt

**The token signature is never checked**

Used by lesson `m05l02`. Graded by `Tokens` in `contract_test.py`.

## What goes wrong

A token whose payload has been edited to another subject is accepted, because only the claims are read.

## The loop

```sh
cd sample-api
patch -p1 < breakages/08-unverified-jwt/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k Tokens          # the suite fails here
patch -p1 -R < breakages/08-unverified-jwt/break.patch  # put it back
python3 contract_test.py -k Tokens          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
