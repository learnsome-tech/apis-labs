"""A loader for the YAML subset openapi.yaml is written in.

PyYAML is not installed on the machine this course is built on, and the course
promises the standard library or one dependency, so the specification is parsed
here instead. The subset is deliberate and small:

    mappings          key: value, nested by two-space indentation
    sequences         - scalar, or - key: value for a mapping item
    scalars           integers, true, false, null, 'quoted', "quoted", plain
    comments          a line whose first non-blank character is a hash

Anything outside that raises, loudly, rather than guessing: a specification
that silently half-parsed would be worse than no specification at all.
"""


class SpecError(ValueError):
    """The specification is outside the subset this loader accepts."""


def scalar(text):
    text = text.strip()
    if text in ('null', '~', ''):
        return None
    if text == 'true':
        return True
    if text == 'false':
        return False
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
        return text[1:-1]
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    if text[0] in '[{|>&*!%':
        raise SpecError(f'unsupported YAML construct: {text[:20]}')
    return text


def rows(text):
    """Every content line as (indent, body), comments and blanks dropped."""
    out = []
    for number, raw in enumerate(text.split('\n'), start=1):
        body = raw.strip()
        if not body or body.startswith('#'):
            continue
        if '\t' in raw[:len(raw) - len(raw.lstrip())]:
            raise SpecError(f'line {number}: tab in indentation')
        out.append((len(raw) - len(raw.lstrip()), body, number))
    return out


def load(text):
    lines = rows(text)
    value, end = parse(lines, 0, lines[0][0] if lines else 0)
    if end != len(lines):
        raise SpecError(f'line {lines[end][2]}: unexpected indentation')
    return value


def parse(lines, start, indent):
    """Parse the block at `indent` beginning at `start`; return value and end."""
    if lines[start][1].startswith('- '):
        return sequence(lines, start, indent)
    return mapping(lines, start, indent)


def sequence(lines, start, indent):
    items = []
    i = start
    while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith('- '):
        body = lines[i][1][2:]
        inner = indent + 2
        if ':' in body and not body.split(':', 1)[0].strip().startswith(('"', "'")):
            key, rest = body.split(':', 1)
            item = {key.strip(): scalar(rest)} if rest.strip() else {}
            i += 1
            if not rest.strip():
                if i < len(lines) and lines[i][0] > inner:
                    raise SpecError(f'line {lines[i][2]}: over-indented')
                item[key.strip()], i = parse(lines, i, lines[i][0]) if i < len(lines) and lines[i][0] == inner + 2 else (None, i)
            while i < len(lines) and lines[i][0] == inner:
                more, i = mapping(lines, i, inner)
                item.update(more)
            items.append(item)
            continue
        items.append(scalar(body))
        i += 1
    return items, i


def mapping(lines, start, indent):
    out = {}
    i = start
    while i < len(lines) and lines[i][0] == indent:
        body = lines[i][1]
        if body.startswith('- '):
            break
        if ':' not in body:
            raise SpecError(f'line {lines[i][2]}: not a key and value')
        key, rest = body.split(':', 1)
        key = scalar(key) if key.strip()[0] in ('"', "'") else key.strip()
        i += 1
        if rest.strip():
            out[key] = scalar(rest)
            continue
        if i < len(lines) and lines[i][0] > indent:
            out[key], i = parse(lines, i, lines[i][0])
        else:
            out[key] = None
    return out, i
