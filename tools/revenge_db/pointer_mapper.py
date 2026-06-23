from data.wrestlers import WRESTLERS


def parse_pointer(value):
    if not value:
        return None

    return int(value, 16)


def pointer_delta(start, end):
    if start is None or end is None:
        return None

    return end - start


def print_pointer_map(wrestler):
    name_pointer = parse_pointer(wrestler["name_pointer"])
    height_pointer = parse_pointer(wrestler["height_pointer"])
    weight_pointer = parse_pointer(wrestler["weight_pointer"])
    stable_pointer = parse_pointer(wrestler["stable_pointer"])

    print(wrestler["name"])
    print(f'ID2: {wrestler["id2"]}')
    print(f'ID4: {wrestler["id4"]}')
    print(f'Name Pointer: {wrestler["name_pointer"]}')
    print(f'Height Pointer: {wrestler["height_pointer"]}')
    print(f'Weight Pointer: {wrestler["weight_pointer"]}')
    print(f'Stable Pointer: {wrestler["stable_pointer"]}')
    print(f'Stable - Name Delta: 0x{pointer_delta(name_pointer, stable_pointer):X}')


def main():
    for wrestler in WRESTLERS.values():
        if wrestler.get("stable_pointer"):
            print_pointer_map(wrestler)


if __name__ == "__main__":
    main()