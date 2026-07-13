import sys

SIZE = 10
hash_table = [-1] * SIZE


def method_name(method):
    if method == 1:
        return "Linear Probing"
    return "Quadratic Probing"


def get_index(value, i, method):
    base = value % SIZE

    if method == 1:
        return (base + i) % SIZE
    else:
        return (base + i * i) % SIZE


def insert(value, method):
    for i in range(SIZE):
        index = get_index(value, i, method)

        if hash_table[index] == -1:
            hash_table[index] = value
            print(f"Value {value} inserted successfully using {method_name(method)}.")
            return

    print("Hash table is full. Insertion failed.")


def search(value, method):
    for i in range(SIZE):
        index = get_index(value, i, method)

        if hash_table[index] == value:
            print(f"Value {value} found at index {index} using {method_name(method)}.")
            return

        if hash_table[index] == -1:
            break

    print(f"Value {value} not found using {method_name(method)}.")


for line in sys.stdin:
    parts = line.strip().split()

    if not parts:
        continue

    try:
        choice = int(parts[0])
    except ValueError:
        print("Invalid choice.")
        continue

    if choice == 1 or choice == 2:
        if len(parts) != 3:
            print("Invalid choice.")
            continue

        try:
            value = int(parts[1])
            method = int(parts[2])
        except ValueError:
            print("Invalid choice.")
            continue

        if method not in (1, 2):
            print("Invalid probing method.")
            continue

        if choice == 1:
            insert(value, method)
        else:
            search(value, method)

    elif choice == 3:
        print(*hash_table)

    elif choice == 4:
        break

    else:
        print("Invalid choice.")