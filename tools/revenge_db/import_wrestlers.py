import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "exports" / "wrestler_master.csv"
OUTPUT_PATH = ROOT / "data" / "wrestlers.py"


def parse_championships(value):
    if not value:
        return []

    return [item.strip() for item in value.split("|") if item.strip()]


def parse_optional_hex(value):
    value = value.strip()

    if not value or value.lower() == "verify":
        return None

    return value


def main():
    wrestlers = {}

    with CSV_PATH.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if not row.get("id2"):
                continue

            id2_hex = row["id2"].strip()
            id2 = int(id2_hex, 16)

            wrestlers[id2] = {
                "name": row["name"],
                "id2": id2_hex,
                "id2_decimal": id2,
                "id4": row["id4"],
                "manager_id2": parse_optional_hex(row["manager_id2"]),
                "name_pointer": row["name_pointer"],
                "height_pointer": row["height_pointer"],
                "weight_pointer": row["weight_pointer"],
                "stable_pointer": row["stable_pointer"],
                "music": row["music"],
                "championships": parse_championships(row["championships"]),
            }

    OUTPUT_PATH.write_text(
        "WRESTLERS = " + repr(wrestlers) + "\n",
        encoding="utf-8",
    )

    print(f"Imported {len(wrestlers)} wrestlers.")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()