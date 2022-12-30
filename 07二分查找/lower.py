# -*- encoding=utf-8 -*-

def lower(nums, target):
    # 使用二分搜索法寻找小于target的索引最大值
    left = -1
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    array = ArrayGenerator.generate_ordered_array(10)
    target = 3
    print(lower(array, target))
