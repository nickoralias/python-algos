def quick_sort(arr):
    if not arr:
        return arr
       
    i, j = 1, len(arr)-1 
    pivot_index = random.randint(0, j)
    pivot_value = arr[pivot_index]
    tmp = arr[0]
    arr[0] = pivot_value
    arr[pivot_index] = tmp
    
    while (i <= j):
        if arr[i] < pivot_value:
            i += 1
        elif arr[j] > pivot_value:
            j -= 1
        else:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1

    arr[0] = arr[j]
    arr[j] = pivot_value
    left = quick_sort(arr[0:j])
    right = quick_sort(arr[j+1:len(arr)])
    return left + [arr[j]] + right
