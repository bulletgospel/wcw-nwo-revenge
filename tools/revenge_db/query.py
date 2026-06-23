import sys

from data.wrestlers import WRESTLERS


MANAGERS = {
    "00": "None",
    "40": "Hollywood Hogan",
    "41": "Yugi Nagata",
    "42": "Barbarian / Meng",
    "43": "Curt Hennig",
    "44": "Scott Hall",
    "47": "Brian Adams / Scott Norton / Scott Steiner",
    "48": "Eric Bischoff / Macho Man Randy Savage",
    "49": "Diamond Dallas Page",
}


def print_wrestler(wrestler):
    manager_id = wrestler["manager_id2"]
    manager_name = MANAGERS.get(manager_id, "Unknown")

    print(wrestler["name"])
    print(f'ID2: {wrestler["id2"]}')
    print(f'ID4: {wrestler["id4"]}')
    print(f"Manager: {manager_id} ({manager_name})")
    print(f'Music: {wrestler["music"]}')
    print(f'Championships: {", ".join(wrestler["championships"])}')


def query_wrestler_by_id(wrestler_id):
    wrestler = WRESTLERS.get(wrestler_id)

    if not wrestler:
        print("Wrestler not found.")
        return

    print_wrestler(wrestler)


def query_wrestler_by_name(search_text):
    search_text = search_text.lower()

    for wrestler in WRESTLERS.values():
        if search_text in wrestler["name"].lower():
            print_wrestler(wrestler)
            return

    print("Wrestler not found.")


def query_manager(manager_id):
    manager = MANAGERS.get(manager_id)

    if not manager:
        print("Manager not found.")
        return

    print(manager)
    print(f"Manager ID2: {manager_id}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("python -m tools.revenge_db.query wrestler 15")
        print('python -m tools.revenge_db.query wrestler "Hollywood Hogan"')
        print("python -m tools.revenge_db.query manager 40")
        sys.exit()

    category = sys.argv[1]
    query = " ".join(sys.argv[2:])

    if category == "wrestler":
        if query.isdigit():
            query_wrestler_by_id(int(query))
        else:
            query_wrestler_by_name(query)

    elif category == "manager":
        query_manager(query)

    else:
        print("Supported categories: wrestler, manager")