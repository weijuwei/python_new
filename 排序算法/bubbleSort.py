# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1,i,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr


if __name__ == "__main__":
    arr = [55, 23, 53, 36, 56, 10, 28, 100, 59, 98, 78]
    print("排序前：",arr)
    arr1 = bubble_sort(arr)
    print("排序后：",arr1)