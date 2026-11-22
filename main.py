"""Write one short text to /output/entry.txt.

The text is a literal in this file. It runs with the Python
standard library only, makes no network calls, and always
writes the same bytes.
"""

import os

TEXT = (
    "In the wall of the old post office there is a drawer no key opens. "
    "Every morning it holds one letter, addressed to whoever opens it, "
    "and the handwriting is always your own."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
