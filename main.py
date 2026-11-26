"""One Line, One Laugh.

A smart speaker hears everything, so confiding in one is a bad idea with
an obvious punchline: the ads know, and now they are worried about you.
One line, one joke, no setup left over.

Running this file writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "I whispered a secret to my smart speaker and now it suggests therapy "
    "ads in the same gentle voice my mother uses."
)


def get_entry() -> str:
    """Return the funny line."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
