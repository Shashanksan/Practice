import sys

heap = []


def insert(value):
    heap.append(value)
    i = len(heap) - 1

    # Move the inserted element upward
    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break


def extract_max():
    if not heap:
        return None

    max_value = heap[0]
    last = heap.pop()

    if heap:
        heap[0] = last
        i = 0

        # Move the root downward
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < len(heap) and heap[left] > heap[largest]:
                largest = left

            if right < len(heap) and heap[right] > heap[largest]:
                largest = right

            if largest == i:
                break

            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest

    return max_value


for line in sys.stdin:
    parts = line.strip().split()

    if not parts:
        continue

    try:
        choice = int(parts[0])
    except ValueError:
        print("Invalid choice.")
        continue

    if choice == 1:
        if len(parts) != 2:
            print("Invalid insertion command.")
            continue

        try:
            value = int(parts[1])

            if value <= 0:
                print("Invalid insertion command.")
            else:
                insert(value)
                print(f"Element {value} inserted into the heap.")

        except ValueError:
            print("Invalid insertion command.")

    elif choice == 2:
        value = extract_max()

        if value is None:
            print("Heap is empty. No elements to extract.")
        else:
            print(f"Highest priority element {value} extracted.")

    elif choice == 3:
        if not heap:
            print("Heap is empty.")
        else:
            print(*heap)

    elif choice == 4:
        break

    else:
        print("Invalid choice.")