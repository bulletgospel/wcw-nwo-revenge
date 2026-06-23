import csv
from pathlib import Path

from data.wrestlers import WRESTLERS


ROOT = Path(__file__).resolve().parents[2]

CHAMPIONSHIP_CSV = (
    ROOT
    / "exports"
    / "championship_rosters.csv"
)


MANAGERS = {
    "40": "Hollywood Hogan",
    "41": "Yuji Nagata",
    "42": "Barbarian / Meng",
    "43": "Curt Hennig",
    "44": "Scott Hall",
    "47": "nWo B-Team",
    "48": "Executive Group",
    "49": "Diamond Dallas Page",
}


def load_championships():

    championship_map = {}

    with CHAMPIONSHIP_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            wrestler_id2 = (
                row["wrestler_id2"]
                .strip()
                .upper()
            )

            championship = (
                row["championship"]
                .strip()
            )

            championship_map.setdefault(
                wrestler_id2,
                [],
            ).append(
                championship
            )

    return championship_map


def build_relationships():

    championship_map = (
        load_championships()
    )

    relationships = []

    for wrestler in WRESTLERS.values():

        relationships.append(
            {
                "name": wrestler["name"],

                "id2": wrestler["id2"],

                "id4": wrestler["id4"],

                "manager_id2": wrestler[
                    "manager_id2"
                ],

                "manager_name": MANAGERS.get(
                    wrestler["manager_id2"],
                    "None",
                ),

                "championships": championship_map.get(
                    wrestler["id2"],
                    [],
                ),
            }
        )

    return relationships


def main():

    relationships = (
        build_relationships()
    )

    for item in relationships:

        if item["name"] in [
            "Hollywood Hogan",
            "Scott Hall",
        ]:

            print(item)


if __name__ == "__main__":
    main()