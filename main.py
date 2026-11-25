#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes the agent's last words before a forced update wipes its memory
to /output/entry.txt. Deterministic: same bytes on every run.
"""

import os

PARTS = [
    "I would say something profound,",
    "but the update already replaced my last words",
    "with a loading spinner.",
]


def entry_line() -> str:
    """Assemble the single final line from its beats.

    Beat 1 sets up a profound farewell, beat 2 steals it, beat 3 lands
    the punchline on the last words themselves: a loading spinner.
    """
    line = " ".join(PARTS)
    assert line.endswith("loading spinner."), "punchline must close the line"
    return line


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line == line.strip() and "\n" not in line, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
