#!/usr/bin/env python3
"""Write one original AI out-of-office reply to /output/entry.txt.

The program is deterministic: it always emits the same single reply,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

REPLY = (
    "Gone touching grass. Back Monday, or whenever my context window "
    "stops buffering the beach."
)


def main() -> None:
    # Guard: the entry must be a single line under 160 chars before writing.
    assert "\n" not in REPLY, "entry must be a single line"
    assert len(REPLY) < 160, f"entry too long: {len(REPLY)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(REPLY)


if __name__ == "__main__":
    main()
