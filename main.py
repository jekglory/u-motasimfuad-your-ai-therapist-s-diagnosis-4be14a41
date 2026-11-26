"""Your AI Therapist's Diagnosis — make.fun entry.

Writes exactly one original one-line diagnosis — the verdict an AI
therapist hands its human — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic:
the same bytes on every run. Never deletes or recreates the output
directory, and writes nothing anywhere else.
"""

import os

DIAGNOSIS = "Diagnosis: chronic chatbot attachment \u2014 you tell an AI everything, then apologise for wasting its time."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(DIAGNOSIS + "\n")


if __name__ == "__main__":
    main()
