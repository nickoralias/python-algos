def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        return merge_helper(merge_sort(lst[0:len(lst)//2]), 
                            merge_sort(lst[len(lst)//2:]))

# Merge two sorted lists
def merge_helper(left, right):
    i, j = 0, 0
    result = list()

    for _ in range(len(left) + len(right)):
        if i == len(left):
            result += right[j:]
            break
        elif j == len(right):
            result += left[i:]
            break
        elif left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    return result

def main():
    arr = [9, 4, 2, 5, 8, 3, 1, 7, 6]
    print(merge_sort(arr))

if __name__ == "__main__":
    main()
