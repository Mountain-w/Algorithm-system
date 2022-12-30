# -*- encoding=utf-8 -*-


def lower_ceil(nums, target):
    # 如果数组中存在target，返回最小索引
    # 如果数组中不存在，返回upper
    left = 0
    right = len(nums)
    # 循环不变量 nums[left, right)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
