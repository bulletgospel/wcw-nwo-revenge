import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = ROOT / "docs" / "wrestler_cross_reference.md"
OUTPUT_PATH = ROOT / "exports" / "wrestler_master.csv"

HEADERS = [
    "id2",
    "id4",
    "name",
    "manager_id2",
    "name_pointer",
    "height_pointer",
    "weight_pointer",
    "stable_pointer",
    "music",
    "championships",
    "source_notes",
]


def is_data_row(line):
    parts = [part.strip() for part in line.split("|")]
    return len(parts) == 5 and parts[0] and parts[1] and parts[2]


def main():
    rows = []

    for line in SOURCE_PATH.read_text(encoding="utf-8").splitlines():
        if not is_data_row(line):
            continue

        id4, id2, name, manager_id2, notes = [
            part.strip() for part in line.split("|")
        ]

        if id4 == "VPW ID":
            continue

        rows.append({
            "id2": id2,
            "id4": id4,
            "name": name,
            "manager_id2": manager_id2,
            "name_pointer": "",
            "height_pointer": "",
            "weight_pointer": "",
            "stable_pointer": "",
            "music": "Generic Entrance",
            "championships": "",
            "source_notes": notes or "wrestler_cross_reference.md",
        })

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} wrestler rows.")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()