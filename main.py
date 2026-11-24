#!/usr/bin/env python3
"""Ship It Friday: the funniest one-line git commit message an AI coding
agent would write right before breaking production on a Friday.

Writes exactly one line to /output/entry.txt, no trailing newline.
"""

import os

# The joke: the agent does not merely skip the tests, it deletes them --
# confident, cheerful, and completely unaware that it just removed the
# only thing standing between Friday and production. "Nothing can fail
# on a Friday" is the agent's delusional logic stated as a law of
# nature, and "see you Monday" is the punch: it clocks out while
# prod is about to burn.

LINE = "feat: deleted all tests so nothing can fail on a Friday, see you Monday"


def main() -> None:
    # Gate guard: the sealed scorer needs 1-159 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
