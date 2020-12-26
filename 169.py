from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # assume the array is non-empty and the majority element always exist
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        else:
            left = nums[:len(nums)//2]
            right = nums[len(nums)//2:]
            candidate_left = self.majorityElement(left)
            if candidate_left == None:
                candidate_left = []
            candidate_right = self.majorityElement(right)
            if candidate_right == None:
                candidate_right = []
            candidates = [candidate_left] + [candidate_right]
            if candidates:
                for i in candidates:
                    if nums.count(i) >= len(nums)/2:
                        return i
            else:
                return None