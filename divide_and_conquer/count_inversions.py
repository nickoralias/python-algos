#  https://leetcode.com/problems/global-and-local-inversions/
inversions = []

def count_inversions(lst):
    if len(lst) <= 1:
        return lst
    else:
        return merge_and_add_inversions(count_inversions(lst[0:len(lst)//2]),
                            count_inversions(lst[len(lst)//2:]))

# Merge and record inversions
def merge_and_add_inversions(left, right):
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
            for x in left[i:]:
                inversions.append((x, right[j]))
            j+=1

    return result

def main():
    #arr = [9, 4, 2, 5, 8, 3, 1, 7, 6]
    arr = [1,3,5,2,4,6]
    #print(count_inversions(arr))
    count_inversions(arr)
    print(inversions)

if __name__ == "__main__":
    main()
