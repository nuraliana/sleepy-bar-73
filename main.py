"""Loading Screen Gold: a one-line loading-screen tip.

The program holds the tip in TIP and writes it to a file called
entry.txt inside the directory named by the MAKEFUN_OUTPUT_DIR
environment variable when set, falling back to a local entry.txt
next to this file when unset.

Standard library only. Deterministic: the same text every run.
"""

import os

TIP = "Tip: your agent's six-step plan starts with 'understand the codebase.' It's still on step one. So are you."


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    with open(output_path(), "w", encoding="utf-8") as handle:
        handle.write(TIP)


if __name__ == "__main__":
    main()
