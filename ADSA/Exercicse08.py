def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


try:
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) != n:
        print("Error: Mismatch between count and number of elements.")
    else:
        while True:
            choice = int(input())

            if choice == 1:
                print(*quick_sort(arr.copy()))

            elif choice == 2:
                print(*merge_sort(arr.copy()))

            elif choice == 3:
                print("Quick Sort Time Complexity:")
                print("Best Case: O(n log n)")
                print("Average Case: O(n log n)")
                print("Worst Case: O(n^2)")
                print()
                print("Merge Sort Time Complexity:")
                print("Best Case: O(n log n)")
                print("Average Case: O(n log n)")
                print("Worst Case: O(n log n)")

            elif choice == 4:
                break

            else:
                print("Invalid choice.")

except Exception as e:
    print("Error:", e)