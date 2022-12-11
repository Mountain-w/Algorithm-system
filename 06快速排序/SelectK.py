from random import randint


# 找到数组中第 K 大的数
class SelectKB:
    @staticmethod
    def select_k(nums, k):
        return SelectKB._sort(nums, 0, len(nums) - 1, len(nums) - k)

    @staticmethod
    def _sort(nums, left, right, k):
        if left >= right:
            return nums[left]
        l, r = SelectKB.partition(nums, left, right)
        if k > r:
            return SelectKB._sort(nums, r + 1, right, k)
        elif k < l:
            return SelectKB._sort(nums, left, l - 1, k)
        else:
            return nums[l]

    @staticmethod
    def partition(nums, left, right):
        p = randint(left, right)
        nums[p], nums[right] = nums[right], nums[p]
        lt = left - 1
        gt = right
        l = left
        while l < gt:
            if nums[l] < nums[right]:
                lt += 1
                nums[lt], nums[l] = nums[l], nums[lt]
                l += 1
            elif nums[l] > nums[right]:
                gt -= 1
                nums[gt], nums[l] = nums[l], nums[gt]
            else:
                l += 1
        nums[gt], nums[right] = nums[right], nums[gt]
        return lt + 1, gt


# 找到数组中第 K 小的数
class SelectKS:
    @staticmethod
    def select_k(nums, k):
        return SelectKS._sort(nums, 0, len(nums) - 1, k - 1)

    @staticmethod
    def _sort(nums, left, right, k):
        if left >= right:
            return nums[left]
        l, r = SelectKS.partition(nums, left, right)
        if k > r:
            return SelectKS._sort(nums, r + 1, right, k)
        elif k < l:
            return SelectKS._sort(nums, left, l - 1, k)
        else:
            return nums[l]

    @staticmethod
    def partition(nums, left, right):
        p = randint(left, right)
        nums[p], nums[right] = nums[right], nums[p]
        lt = left - 1
        gt = right
        l = left
        while l < gt:
            if nums[l] < nums[right]:
                lt += 1
                nums[lt], nums[l] = nums[l], nums[lt]
                l += 1
            elif nums[l] > nums[right]:
                gt -= 1
                nums[gt], nums[l] = nums[l], nums[gt]
            else:
                l += 1
        nums[gt], nums[right] = nums[right], nums[gt]
        return lt + 1, gt


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    array = ArrayGenerator.generate_random_array(10, 0, 100)
    array2 = array.copy()
    print("第 k 大的数")
    print(array)
    print(SelectKB.select_k(array, 3))
    array.sort()
    print(array[-3])
    print("第 k 小的数")
    print(array2)
    print(SelectKS.select_k(array2, 3))
    array2.sort()
    print(array2[2])
