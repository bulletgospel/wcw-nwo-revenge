from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = ROOT / "docs" / "championship_architecture.md"
OUTPUT_PATH = ROOT / "exports" / "championship_rosters.csv"


def main():
    text = SOURCE_PATH.read_text(encoding="utf-8")

    print("Championship source loaded.")
    print(f"Characters read: {len(text)}")
    print(f"Source: {SOURCE_PATH}")
    print(f"Target CSV: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()