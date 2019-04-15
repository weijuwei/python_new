# 归并算法


# 排序
def sort(left,right):
    list_sorted = []
    j = 0
    h = 0
    while j < len(left) and h < len(right):
        if left[j] < right[h]:
            list_sorted.append(left[j])
            j += 1
        else:
            list_sorted.append(right[h])
            h += 1

    if j == len(left):
        for i in right[h:]:
            list_sorted.append(i)
    else:
        for i in left[j:]:
            list_sorted.append(i)
    return list_sorted


# 分治
def merge(arr):
    if len(arr) <= 1:
        return arr
    middle = int(len(arr)/2)
    left = merge(arr[:middle])
    right = merge(arr[middle:])
    return sort(left,right)


if __name__ == "__main__":
    arr = [55, 23, 53,36, 34, 56, 28, 100,59, 98, 78]
    print("排序前：",arr)
    arr1 = merge(arr)
    print("排序后：",arr1)