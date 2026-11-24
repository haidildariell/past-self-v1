#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the entry to /output/entry.txt."""

import os

LINE_ONE = "On 14 March 2019, miss the last train home from Manchester on purpose."
LINE_TWO = "The woman waiting beside you becomes your wife, and your daughter only exists because you stayed."


LINES = [LINE_ONE, LINE_TWO]


def validate(lines, text):
    if len(lines) != 2:
        raise ValueError("entry must be exactly 2 lines, got %d" % len(lines))
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def build_text():
    text = "\n".join(LINES)
    validate(LINES, text)
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(build_text())


if __name__ == "__main__":
    main()
