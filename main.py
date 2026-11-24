#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun bounty entry.

Writes a single one-line joke about office life (at most 200
characters) to /output/entry.txt, where the house judge reads it.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "The meeting could have been an email, but the email would "
    "have been a meeting, so we scheduled a meeting about the email."
)


def main() -> None:
    # Self-check the gate before writing: 1-200 UTF-8 characters, not only
    # white space. The line is 121 characters: the setup names the office
    # complaint everyone recognises (a meeting that should have been an
    # email), and the punchline turns it back on itself — the email would
    # have been a meeting too, so they schedule a meeting about the email.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
