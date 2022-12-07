def merge(arr, left, mid, right, temp):
    index = 0
    l_p = left
    r_p = mid + 1
    while l_p <= mid and r_p <= right:
        if arr[l_p] <= arr[r_p]:
            temp[index] = arr[l_p]
            l_p += 1
        else:
            temp[index] = arr[r_p]
            r_p += 1
        index += 1
    while l_p <= mid:
        temp[index] = arr[l_p]
        l_p += 1
        index += 1
    while r_p <= right:
        temp[index] = arr[r_p]
        r_p += 1
        index += 1
    for i in range(index):
        arr[left] = temp[i]
        left += 1


def _merge_sort(arr, left, right, temp, level):
    if left >= right:
        return
    mid = left + ((right - left) >> 1)
    _merge_sort(arr, left, mid, temp, level + 1)
    _merge_sort(arr, mid + 1, right, temp, level + 1)
    if arr[mid] > arr[mid + 1]:  # 对于左右两边已经有序的情况就不调用合并，优化有序数组的情况
        merge(arr, left, mid, right, temp)


def merge_sort(arr):
    left = 0
    right = len(arr) - 1
    temp = [0] * len(arr)
    _merge_sort(arr, left, right, temp, 0)


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator
    array = ArrayGenerator.generate_random_array(10, 0, 100)
    print(array)
    merge_sort(array)
    print(array)
