#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign, at most 120 characters, to /output/entry.txt.
The sign is written for the door of a haunted server room: an
all-caps posted notice whose joke is the collision of office IT life
(a lost root password) with the supernatural (the ghost in Rack 7 is
the only one who still knows it).
"""

import os

MAX_CHARS = 120

ENTRY = "DO NOT EXORCISE THE GHOST IN RACK 7 \u2014 he\u2019s the only one who still knows the root password."


def validate(entry):
    """A door sign is exactly one line: 1-120 chars, no newline, no padding."""
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= MAX_CHARS, (
        f"entry is {len(entry)} chars, must be 1-{MAX_CHARS}"
    )
    assert entry.strip(), "entry must not be only whitespace"
    return entry


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
