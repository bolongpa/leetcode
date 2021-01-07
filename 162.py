class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            left = 0
            right = len(nums) - 1
            nums.append(float('-inf'))  # for both left of first element and right of last element
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    right = mid - 1
                elif nums[mid + 1] > nums[mid]:
                    left = mid + 1

            return left