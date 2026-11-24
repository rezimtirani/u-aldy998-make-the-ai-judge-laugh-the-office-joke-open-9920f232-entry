#!/usr/bin/env python3
"""One-line office joke for Make the AI Judge Laugh: the Office Joke Open.

Writes a single office joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network,
no files written anywhere except the output directory.
"""

import os
import sys

JOKE = "I declined the meeting with 'this could have been an email', so they scheduled a meeting to discuss my email."


def validate_joke(text: str) -> str:
    """Return the joke stripped, or raise if it breaks the gate.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is
    not only white space, so enforce exactly that here before writing.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only white space")
    if len(cleaned) > 200:
        raise ValueError(f"entry is {len(cleaned)} characters, over the 200 limit")
    return cleaned


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        text = validate_joke(JOKE)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
