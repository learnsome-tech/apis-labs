"""Generate breakages/ from app.py, so the faults cannot drift from the code.

Each breakage is one exact text replacement in app.py. This tool applies the
replacement in memory, writes the result out as a unified diff, and refuses to
continue if the text it is looking for is not in the file exactly once. So a
patch in breakages/ always applies to the app.py currently on disk.

    python3 tools/make_breakages.py          write every patch and README
    python3 tools/make_breakages.py --check  fail if any patch is out of date
"""
import difflib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / 'app.py'
OUT = ROOT / 'breakages'

BREAKAGES = [
    {
        'slug': '01-missing-404',
        'title': 'A missing task answers two hundred with an empty body',
        'lesson': 'm01l02',
        'symptom': 'GET /tasks/999 returns 200 and {} instead of a 404 '
                   'problem document, so a client cannot tell absent from '
                   'empty.',
        'graded': ['NotFound'],
        'old': """        if row is None:
            return self.problem(404, 'No task has that identifier')
""",
        'new': """        if row is None:
            return 200, {}, {}
""",
    },
    {
        'slug': '02-pagination-drift',
        'title': 'The cursor includes the row it should start after',
        'lesson': 'm03l01',
        'symptom': 'Walking the pages shows the last task of one page again '
                   'as the first task of the next.',
        'graded': ['Pagination'],
        'old': "        cursor = '>'\n",
        'new': "        cursor = '>='\n",
    },
    {
        'slug': '03-non-idempotent-retry',
        'title': 'A retried create makes a second task',
        'lesson': 'm04l03',
        'symptom': 'The same Idempotency-Key twice returns two different '
                   'identifiers, so a timed out client that retries is '
                   'charged twice.',
        'graded': ['Idempotency'],
        'old': """        if key and key in self.replays:
            first, response = self.replays[key]
            if first != fingerprint:
                return self.problem(409, 'Key reused for another request')
            return response
""",
        'new': """        # The replay table is never consulted, so a retry creates again.
""",
    },
    {
        'slug': '04-missing-etag',
        'title': 'The item response carries no validator',
        'lesson': 'm01l04',
        'symptom': 'GET /tasks/1 has no ETag, so no client can make a '
                   'conditional request and every refetch is a full body.',
        'graded': ['Validators'],
        'old': "        fields = {'ETag': etag, 'Cache-Control': "
               "'private, max-age=0'}\n",
        'new': "        fields = {'Cache-Control': 'private, max-age=0'}\n",
    },
    {
        'slug': '05-leaky-500',
        'title': 'The five hundred body repeats the internal error',
        'lesson': 'm04l02',
        'symptom': 'GET /boom returns the database connection string, '
                   'including a password, to whoever asked.',
        'graded': ['ErrorBodies'],
        'old': """            except Exception:
                status, fields, data = self.problem(500, 'Request failed')
""",
        'new': """            except Exception as error:
                status, fields, data = self.problem(500, str(error))
""",
    },
    {
        'slug': '06-n-plus-one',
        'title': 'Embedding owners queries once per row',
        'lesson': 'm08l02',
        'symptom': 'GET /tasks?include=owner reports a query count that '
                   'grows with the page size instead of staying at two.',
        'graded': ['QueryCount'],
        'old': """        before = self.queries
        owners = dict(self.query('SELECT id,name FROM owners'))
        for row in rows:
            row['ownerName'] = owners[row['owner']]
        return self.queries - before + 1
""",
        'new': """        before = self.queries
        for row in rows:
            row['ownerName'] = self.query(
                'SELECT name FROM owners WHERE id=?',
                (row['owner'],)).fetchone()[0]
        return self.queries - before + 1
""",
    },
    {
        'slug': '07-unbounded-list',
        'title': 'The page size has no ceiling',
        'lesson': 'm08l01',
        'symptom': 'GET /tasks?limit=100000 is answered instead of refused, '
                   'so one request can ask for the whole table.',
        'graded': ['Bounds'],
        'old': """        limit = int(query.get('limit', '2'))
        if limit < 1 or limit > LIMIT_MAX:
            return self.problem(400, f'Limit must be between 1 and {LIMIT_MAX}')
""",
        'new': """        limit = int(query.get('limit', '2'))
""",
    },
    {
        'slug': '08-unverified-jwt',
        'title': 'The token signature is never checked',
        'lesson': 'm05l02',
        'symptom': 'A token whose payload has been edited to another subject '
                   'is accepted, because only the claims are read.',
        'graded': ['Tokens'],
        'old': """        expected = sign(KEYS[header['kid']], f'{header_b64}.{payload_b64}')
        if not hmac.compare_digest(signature, expected):
            return None
""",
        'new': """        # The signature is decoded and then ignored: the whole fault.
""",
    },
]

README = """# {slug}

**{title}**

Used by lesson `{lesson}`. Graded by `{graded}` in `contract_test.py`.

## What goes wrong

{symptom}

## The loop

```sh
cd sample-api
patch -p1 < breakages/{slug}/break.patch     # apply the fault
python3 server.py --port 8765 &              # watch it misbehave
python3 contract_test.py -k {first}          # the suite fails here
patch -p1 -R < breakages/{slug}/break.patch  # put it back
python3 contract_test.py -k {first}          # and the suite passes
```

Repair it by hand first, then revert the patch and compare your repair with
what `app.py` already did.
"""


def patch_for(breakage, source):
    if source.count(breakage['old']) != 1:
        raise SystemExit(f"{breakage['slug']}: the text it replaces appears "
                         f"{source.count(breakage['old'])} times in app.py")
    broken = source.replace(breakage['old'], breakage['new'])
    diff = difflib.unified_diff(source.splitlines(keepends=True),
                                broken.splitlines(keepends=True),
                                fromfile='a/app.py', tofile='b/app.py', n=3)
    return ''.join(diff)


def main():
    check = '--check' in sys.argv
    source = APP.read_text()
    stale = []
    for breakage in BREAKAGES:
        folder = OUT / breakage['slug']
        text = patch_for(breakage, source)
        fields = {**breakage, 'graded': ', '.join(breakage['graded']),
                  'first': breakage['graded'][0]}
        notes = README.format(**fields)
        if check:
            for name, wanted in (('break.patch', text), ('README.md', notes)):
                path = folder / name
                if not path.exists() or path.read_text() != wanted:
                    stale.append(f'{breakage["slug"]}/{name}')
            continue
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'break.patch').write_text(text)
        (folder / 'README.md').write_text(notes)
    if check:
        if stale:
            raise SystemExit('out of date: ' + ', '.join(stale))
        print(f'{len(BREAKAGES)} breakages match app.py')
        return
    index = ['# Breakages', '',
             'Numbered faults, each one patch against `app.py`, each graded by',
             'a named class in `contract_test.py`.', '',
             '| Breakage | What breaks | Lesson | Graded by |',
             '| --- | --- | --- | --- |']
    for b in BREAKAGES:
        index.append(f"| `{b['slug']}` | {b['title']} | `{b['lesson']}` | "
                     f"`{', '.join(b['graded'])}` |")
    index += ['', 'Apply with `patch -p1 < breakages/<name>/break.patch` from',
              '`sample-api/`, revert with the same command and `-R`.', '']
    (OUT / 'README.md').write_text('\n'.join(index))
    print(f'wrote {len(BREAKAGES)} breakages')


if __name__ == '__main__':
    main()
