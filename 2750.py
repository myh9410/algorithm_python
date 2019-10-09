"""
N = int(input())
arr = []
for i in range(0,N):
    num = int(input())
    arr.append(num)

arr.sort()
for i in range(len(arr)):
    print(arr[i])
"""

"""
삽입정렬
"""

"""
퀵정렬
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def quick_sort2(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    sort(0, len(arr) - 1)
    return arr


N = int(input())
arr = [int(input()) for _ in range(N)]
print(quick_sort2(arr))
