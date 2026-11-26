import os
import sys


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    text = (
        "The chairman of the committee writing the rules for "
        "artificial intelligence just photographed his laptop screen "
        "and emailed the picture to his aide asking her to turn it "
        "into a PDF."
    )
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Force world-readable output so the grader can read it
    # regardless of the process umask.
    os.chmod(output_path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
