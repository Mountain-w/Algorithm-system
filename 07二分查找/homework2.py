
def lower_floor(nums, target):
    # 如果数组中存在target，返回最小索引
    # 如果数组中不存在target，返回lower
    left = -1
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid - 1


def upper_floor(nums, target):
    # 如果数组中存在target，返回最大索引
    # 如果不存在target，返回lower
    pass