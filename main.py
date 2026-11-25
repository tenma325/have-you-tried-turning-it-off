#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry: writes one line of text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = 'Have you tried turning it off and accepting that some things, like this printer and your weekend plans, were never coming back on?'


def main() -> None:
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
