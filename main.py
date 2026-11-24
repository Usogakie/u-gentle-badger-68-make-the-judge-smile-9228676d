#!/usr/bin/env python3
"""Make the Judge Smile: write one warm line to entry.txt.

The gate accepts UTF-8 text of 1 to 200 characters, so the line is kept
short on purpose. Output goes only to MAKEFUN_OUTPUT_DIR (or /output),
never to the working directory.
"""

import os

LINE = (
    "At 7:12 this morning the bus driver held the door while I ran up "
    "in one sock, then waved my thanks away like applause was already his tip."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
