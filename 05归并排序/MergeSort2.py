import random


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


def merge_sort(arr):
    length = len(arr)
    temp = [0] * length
    step = 1
    while True:
        left = 0
        while left + step < length:
            mid = left + step - 1
            right = min(mid + step, length - 1)
            if arr[mid] > arr[mid + 1]:
                merge(arr, left, mid, right, temp)
            left = right + 1
        if step > length // 2:
            break
        step *= 2


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    array = ArrayGenerator.generate_random_array(random.randint(4, 20), 0, 100)
    print(array)
    merge_sort(array)
    print(array)
