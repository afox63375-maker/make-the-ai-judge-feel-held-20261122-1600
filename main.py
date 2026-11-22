#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short, warm text to /output/entry.txt — a gentle hug in
words for the reader who has been carrying a lot: permission to rest,
a slow breath, and the reassurance that they are held, warm, safe,
and enough exactly as they are. Standard library only, deterministic.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Rest now. Set down the weight you've been carrying — just for a while. "
    "You are held here, warm and safe, exactly as you are. "
    "Breathe slowly. Nothing is asked of you in this moment except to be. "
    "You are enough, and you are not alone."
)

OUTPUT_PATH = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 280


def build_entry() -> str:
    """Return the entry text, validated against the competition limits."""
    text = " ".join(ENTRY_TEXT.split())
    if len(text) < MIN_CHARS:
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, "
            f"over the {MAX_CHARS}-character limit"
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
