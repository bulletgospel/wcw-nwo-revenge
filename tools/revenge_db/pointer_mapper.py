from data.wrestlers import WRESTLERS


def print_pointer_map(wrestler):
    print(wrestler["name"])
    print(f'ID2: {wrestler["id2"]}')
    print(f'ID4: {wrestler["id4"]}')
    print(f'Name Pointer: {wrestler["name_pointer"]}')
    print(f'Height Pointer: {wrestler["height_pointer"]}')
    print(f'Weight Pointer: {wrestler["weight_pointer"]}')
    print(f'Stable Pointer: {wrestler["stable_pointer"]}')


def main():
    for wrestler in WRESTLERS.values():
        if wrestler.get("stable_pointer"):
            print_pointer_map(wrestler)


if __name__ == "__main__":
    main()