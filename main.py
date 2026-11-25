#!/usr/bin/env python3
"""Write one single-line deadline excuse to /output/entry.txt.

The entry is a single sentence, 138 characters, no picture, no link, no
second line. The program is deterministic: it writes the same bytes on
every run, uses no network, and reads nothing outside this file.
"""

import os

LINE = (
    "Someone asked me a quick question at nine and it only let go of me "
    "at noon, by which time the deadline had filed a missing-persons report."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
