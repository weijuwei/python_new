# 插入排序
def insert_sort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr


if __name__ == "__main__":
    arr = [55, 23, 53, 36, 56, 10, 28, 100, 59, 98, 78]
    print("排序前：",arr)
    arr1 = insert_sort(arr)
    print("排序后：",arr1)