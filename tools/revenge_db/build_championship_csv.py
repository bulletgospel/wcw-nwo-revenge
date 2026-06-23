import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

SOURCE_PATH = ROOT / "docs" / "championship_architecture.md"

OUTPUT_PATH = ROOT / "exports" / "championship_rosters.csv"


CHAMPIONSHIP_NAMES = {
    "US HEAVYWEIGHT",
    "CRUISERWEIGHT",
    "TAG TEAM",
    "WORLD HEAVYWEIGHT",
    "TV TITLE",
}


def main():

    rows = []

    current_championship = None

    for line in SOURCE_PATH.read_text(
        encoding="utf-8"
    ).splitlines():

        line = line.strip()

        if not line:
            continue

        if line in CHAMPIONSHIP_NAMES:

            # Keep the original capitalization

            current_championship = line

            continue

        if line == "---":

            current_championship = None

            continue

        if not current_championship:

            continue

        match = re.match(
            r"^([0-9A-F]{2})\s+(.+)$",
            line,
        )

        if not match:

            continue

        wrestler_id2, wrestler_name = match.groups()

        rows.append(
            {
                "championship": current_championship,

                "wrestler_id2": wrestler_id2,

                "wrestler_name": wrestler_name,

                "source_notes": "championship_architecture.md",
            }
        )

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "championship",
                "wrestler_id2",
                "wrestler_name",
                "source_notes",
            ],
        )

        writer.writeheader()

        writer.writerows(rows)

    print(
        f"Wrote {len(rows)} championship roster rows."
    )

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()