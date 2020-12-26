from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        pivot = (right - left) // 2
        if right == -1:
            return 0
        if target > nums[-1]:
            return len(nums)
        elif target == nums[-1]:
            return len(nums) - 1
        if target <= nums[0]:
            return 0
        while left < right - 1:
            if nums[pivot] == target:
                return pivot
            if target > nums[pivot]:
                left = pivot
                pivot = pivot + (right - left) // 2
            elif target < nums[pivot]:
                right = pivot
                pivot = pivot - (right - left) // 2
        if target > nums[pivot]:
            return pivot + 1
        # print(left, pivot, right)
        return pivot

