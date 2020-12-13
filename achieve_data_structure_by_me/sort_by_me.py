"""
冒泡排序
插入排序
选择排序
希尔排序
归并排序
快速排序
桶排序
计数排序
基数排序
"""


# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)):
        flag = True  # 标记有没有交换位置
        for j in range(len(arr)-i-1):  # -i 是每冒泡一次就把最大值排在最后了，-1是因为和相邻元素比较
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break


# 插入排序
def insert_sort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        j = i-1
        while j >= 0 and num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num


# 选择排序
def select_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


# 希尔排序
def shell_sort(arr):
    increa = len(arr) // 2
    while increa > 0:
        for i in range(len(arr)-increa):
            j = i
            num = arr[j + increa]
            while j >= 0 and num < arr[j]:
                arr[j + increa] = arr[j]
                j -= increa
            arr[j + increa] = num
        increa //= 2


# 归并排序
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort((arr[mid:]))

    temp = []
    left_i = right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            temp.append(left[left_i])
            left_i += 1
        else:
            temp.append(right[right_i])
            right_i += 1

    # next_arr = left if left_i < len(left) else right
    # i = left_i if next_arr == left else right_i
    # while i < len(next_arr):
    #     temp.append(next_arr[i])
    #     i += 1
    temp += left[left_i:]
    temp += right[right_i:]
    return temp


# 快速排序
def quick_sort(arr):

    def inner_quick_sort(arr, start, end):
        if (end-start) < 2:
            return arr

        left = start
        for i in range(start, end):
            if arr[i] < arr[end]:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[end] = arr[end], arr[left]
        inner_quick_sort(arr, start, left-1)
        inner_quick_sort(arr, left+1, end)

    return inner_quick_sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 4, 2, 0, -5]
    arr.sort()
    # bubble_sort(arr)
    # insert_sort(arr)
    # select_sort(arr)
    # shell_sort(arr)
    # print(merge_sort(arr))
    quick_sort(arr)
    print(arr)

