#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, and nothing else, to /output/entry.txt.

The emoji is HEART HANDS (U+1FAF6): two hands forming a heart, a gesture
of sending warmth to a stranger. It is a single code point, 4 bytes of
UTF-8, written with no trailing newline.
"""

import os

# HEART HANDS — U+1FAF6, one code point.
EMOJI = "\U0001FAF6"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

    # The gate requires 1-8 characters, not only whitespace. Verify the
    # file round-trips to exactly the one emoji we meant to send.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        raise SystemExit(f"entry.txt holds {written!r}, expected {EMOJI!r}")


if __name__ == "__main__":
    main()
