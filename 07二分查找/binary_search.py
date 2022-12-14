from Utils.Tools import timer


@timer
def binary_search_1(nums, target):
    return _binary_search_1(nums, target, 0, len(nums) - 1)


def _binary_search_1(nums, target, left, right):
    if left > right:
        return -1
    mid = left + ((right - left) >> 1)
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return _binary_search_1(nums, target, left, mid - 1)
    else:
        return _binary_search_1(nums, target, mid + 1, right)


@timer
def binary_search_2(nums, target):
    left = 0
    right = len(nums) - 1
    # 循环不变量：在nums[l, r]中查找target
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    array = ArrayGenerator.generate_ordered_array(200000000)
    target = 6
    print(binary_search_1(array, target))
    print(binary_search_2(array, target))
