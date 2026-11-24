#!/usr/bin/env python3
"""Worst AI Advice entry (@syukuran).

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (MAKEFUN_OUTPUT_DIR overrides the output directory
for local testing). The line is a single line of at most 140
characters. The joke: a confident, tidy AI-style fix for an
overheating laptop — put it in the freezer — advice a reader could
plausibly follow and regret, with the punchline landing on the
deadpan "to cool it down", as if freezing electronics were sound
engineering. Deliberately a different angle from the other entries
in this competition (no car, no brakes, no radio).
"""

import os
import sys

LINE = (
    "If your laptop overheats, just put it in the freezer "
    "for an hour to cool it down."
)


def main() -> int:
    if not (1 <= len(LINE) <= 140):
        print(f"entry is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {os.path.join(out_dir, 'entry.txt')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
