def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    pivot = arr[0]
    less, greater = partition(arr[1:], pivot)
    return quicksort(less) + [pivot] + quicksort(greater)

def partition(arr, pivot):
    less, greater = [], []

    for item in arr:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            pass # implement later to handle arrays with duplicate elements

    return [less, greater]

def main():
    arr = [9, 4, 2, 5, 8, 3, 1, 7, 6]
    print(quicksort(arr))

if __name__ == "__main__":
    main()
