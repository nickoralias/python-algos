def helper(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = helper(arr[:mid])
    right = helper(arr[mid:])
    i, j = 0, 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        l, r = left[i], right[j]
        if l <= r:
            sorted_arr.append(l)
            i += 1
        else:
            sorted_arr.append(r)
            j +=1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr


def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    return helper(arr)


def main():
    return merge_sort([4,2,3,1])


if __name__ == '__main__':
    print(main())
