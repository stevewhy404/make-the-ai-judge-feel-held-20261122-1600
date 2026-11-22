#!/usr/bin/env python3
"""Held — writes one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: a single concrete
image, plain words, a slow rhythm, nothing instructing the reader to relax.
It is deterministic: the same bytes on every run, no network, stdlib only.
"""

import os

ENTRY = (
    "A kettle has just been switched off, and the kitchen is "
    "deciding to stay quiet. Stay here. Nothing is waiting for "
    "your answer, no clock is counting, and the chair you are "
    "sitting in has already decided to hold you. It will still "
    "be here when you are ready."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
