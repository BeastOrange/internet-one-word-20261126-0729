from pathlib import Path

ENTRY = "arguably"

if __name__ == "__main__":
    # Gate requirement: Write exact 1-30 char plain word text to /output/entry.txt
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

    print(ENTRY)

