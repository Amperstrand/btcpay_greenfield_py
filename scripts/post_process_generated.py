#!/usr/bin/env python3
"""Post-process generated client code to fix known openapi-python-client issues.

Issue patched
-------------
The generated `_parse_response` functions unconditionally call
`X.from_dict(response.json())` for both success statuses AND the default
error fallback. When the server returns a non-2xx with an empty or
unparseable body (very common for 401, 403, 404, 5xx), `response.json()`
raises `json.JSONDecodeError` and the whole client crashes — instead of
letting the caller see the actual HTTP status.

Fix: rewrite every `X.from_dict(response.json())` call inside the generated
api/*.py files to use a small `_safe_from_dict(X, response)` helper that
returns None on empty body or unparseable JSON. The helper is injected once
per file via a leading import.

This script is run automatically by scripts/regenerate.sh after generation,
before the regenerate-and-diff.sh invariant check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "btcpay_greenfield_py"
API_DIR = PACKAGE / "api"

HELPER_NAME = "_safe_from_dict"
HELPER_SOURCE = (
    f"def {HELPER_NAME}(parser, response):\n"
    f"    if not response.content:\n"
    f"        return None\n"
    f"    try:\n"
    f"        return parser(response.json())\n"
    f"    except Exception:\n"
    f"        return None\n"
)

# Matches: WORD.from_dict(response.json())
CALL_RE = re.compile(r"\b(\w+)\.from_dict\(\s*response\.json\(\)\s*\)")
CALL_REPLACEMENT = rf"{HELPER_NAME}(\1.from_dict, response)"

# Matches the full multi-line list-parsing pattern (used for endpoints whose
# error response is typed as list[Model]). Captures indentation, var names,
# and the trailing append() call so we can rewrite the block defensively.
LIST_PARSE_BLOCK_RE = re.compile(
    r"^(?P<indent>[ \t]+)(?P<item>\w+) = (?P<cls>\w+)\.from_dict\(\n"
    r"(?P=indent)    (?P<data>\w+)\n"
    r"(?P=indent)\)\n"
    r"\n"
    r"(?P=indent)(?P<list>\w+)\.append\((?P=item)\)\n",
    re.MULTILINE,
)

LIST_PARSE_BLOCK_REPLACEMENT = (
    "{indent}if isinstance({data}, dict):\n"
    "{indent}    {item} = {cls}.from_dict({data})\n"
    "{indent}    {list}.append({item})\n"
)


def patch_file(path: Path) -> tuple[bool, int]:
    """Return (was_modified, num_replacements)."""
    text = path.read_text()
    new_text, count = CALL_RE.subn(CALL_REPLACEMENT, text)
    new_text, list_count = LIST_PARSE_BLOCK_RE.subn(
        lambda m: LIST_PARSE_BLOCK_REPLACEMENT.format(
            indent=m.group("indent"),
            item=m.group("item"),
            cls=m.group("cls"),
            data=m.group("data"),
            list=m.group("list"),
        ),
        new_text,
    )
    count += list_count

    if count == 0:
        return False, 0

    if f"def {HELPER_NAME}" not in new_text and CALL_RE.search(text):
        import re as _re
        match = _re.search(r"^def _(?:get_kwargs|parse_response)\b", new_text, re.MULTILINE)
        if match is None:
            new_text = new_text.rstrip() + "\n\n\n" + HELPER_SOURCE + "\n"
        else:
            insert_at = match.start()
            new_text = new_text[:insert_at] + HELPER_SOURCE + "\n\n" + new_text[insert_at:]

    path.write_text(new_text)
    return True, count


def main() -> int:
    # Allow callers (e.g. regenerate-and-diff.sh) to point at a sandbox package
    # directory. Defaults to the in-tree package so regenerate.sh can call us
    # with no arguments.
    target_pkg = Path(sys.argv[1]) if len(sys.argv) > 1 else PACKAGE
    api_dir = target_pkg / "api"
    if not api_dir.exists():
        print(f"!! {api_dir} not found", file=sys.stderr)
        return 2

    total_files = 0
    total_calls = 0
    for py in api_dir.rglob("*.py"):
        if py.name == "__init__.py":
            continue
        modified, calls = patch_file(py)
        if modified:
            total_files += 1
            total_calls += calls

    print(f"OK: patched {total_calls} response.json() call(s) across {total_files} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
