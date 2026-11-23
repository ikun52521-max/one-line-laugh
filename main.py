#!/usr/bin/env python3
"""The One-Line Laugh -- a single funny line, written to /output/entry.txt.

The line is fixed text: no randomness, no clock, no network, so every run
produces byte-identical output.
"""

import os

LINE = (
    "My phone's screen-time report says I spent six hours on my phone "
    "today, so I deleted the app that wrote the report."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """The gate needs 1-200 characters of non-blank text; the judge needs
    one single sentence, so exactly one terminal stop, at the very end."""
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    assert line.strip(), "entry line must not be only whitespace"
    assert line == line.strip(), "entry line must have no leading/trailing space"
    assert line.endswith("."), "entry line must end with a full stop"
    assert line.count(".") == 1, "entry line must be a single sentence"


def main() -> None:
    validate_line(LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The grader collects the file as another user, so it must be readable.
    os.chmod(OUTPUT_PATH, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
