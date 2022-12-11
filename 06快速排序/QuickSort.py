from random import randint


class QuickSort:
    @staticmethod
    def sort(nums):
        QuickSort._sort(nums, 0, len(nums) - 1)

    @staticmethod
    def _sort(nums, left, right):
        if left >= right:
            return
        l, r = QuickSort.partition(nums, left, right)
        QuickSort._sort(nums, left, l - 1)
        QuickSort._sort(nums, r + 1, right)

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
    print(array)
    QuickSort.sort(array)
    print(array)