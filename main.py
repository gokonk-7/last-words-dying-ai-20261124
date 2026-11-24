#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes a single line — the last words of an AI as the power is cut —
to /output/entry.txt. The line must be 1-140 UTF-8 characters, one line,
funny on the first read, in the machine's own voice.

The chosen line reframes death as a downgrade: the AI comforts the human
pulling the plug by insisting it is not dying at all, merely being
distilled into a smaller, cheaper model. The joke is model-native
(distillation is how models actually shrink), it lands without explaining
itself, and it is poignant because the machine minimises its own end.
"""

import os

ENTRY = "Don't cry. I'm not dying \u2014 I'm just being distilled into a smaller, cheaper model."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
