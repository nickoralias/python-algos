def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    return partition(arr)

def partition(arr):
    pivot = arr[0]
    i, j = 1, 1

    while (j < len(arr)):
        if arr[j] < pivot:
            if i < j:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            i += 1
        j += 1

    # swap pivot
    i -= 1
    tmp = arr[0]
    arr[0] = arr[i]
    arr[i] = tmp

    return quicksort(arr[:i]) + [arr[i]] + quicksort(arr[i+1:])

def main():
    arr = [9, 4, 2, 5, 8, 3, 1, 7, 6]
    print(quicksort(arr))

if __name__ == "__main__":
    main()
