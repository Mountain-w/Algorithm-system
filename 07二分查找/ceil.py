# -*- encoding=utf-8 -*-


def ceil(nums, target):
    # 如果数组中存在target返回最大索引
    # 如果数据中不存在target，返回upper
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    if left > 0 and nums[left - 1] == target:
        return left - 1
    return left
