# -*- encoding=utf-8 -*-
# 使用二分查找法寻找大于target的最小值


def upper(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    array = ArrayGenerator.generate_ordered_array(10)
    target = 3
    print(upper(array, target))