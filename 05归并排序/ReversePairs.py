# 查找数组中的逆序对
# 修改归并排序的 merge 函数即可
def reverse_pairs(nums):
    temp = [0] * len(nums)
    return merge_sort(nums, 0, len(nums) - 1, temp)


def merge_sort(nums, left, right, temp):
    if left >= right:
        return 0
    mid = left + ((right - left) >> 1)
    res = 0
    res += merge_sort(nums, left, mid, temp)
    res += merge_sort(nums, mid + 1, right, temp)
    if nums[mid] > nums[mid + 1]:
        res += merge(nums, left, mid, right, temp)
    return res


def merge(nums, left, mid, right, temp):
    index = 0
    res = 0
    l_p = left
    r_p = mid + 1
    while l_p <= mid and r_p <= right:
        if nums[l_p] <= nums[r_p]:
            temp[index] = nums[l_p]
            l_p += 1
        else:
            res += mid - l_p + 1
            temp[index] = nums[r_p]
            r_p += 1
        index += 1
    while l_p <= mid:
        temp[index] = nums[l_p]
        index += 1
        l_p += 1
    while r_p <= right:
        temp[index] = nums[r_p]
        index += 1
        r_p += 1
    for i in range(index):
        nums[left] = temp[i]
        left += 1
    return res
