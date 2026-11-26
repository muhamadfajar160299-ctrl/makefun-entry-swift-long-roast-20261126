#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (181 characters) to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only; deterministic; no network access.
"""

import os
import sys

ENTRY = "The chairman of the committee writing the rules for artificial intelligence just photographed his laptop screen and emailed the picture to his aide asking her to turn it into a PDF."
# One sentence only: the setup is the chairman's authority over AI rules,
# the turn is the photographed screen, and the punch lands on the last words.


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
