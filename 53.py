from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            left = nums[:len(nums) // 2]
            right = nums[len(nums) // 2:]

            left_max_subarray = self.maxSubArray(left)
            right_max_suvarray = self.maxSubArray(right)

            # find max subarray cross mid
            # max subarray in left with right at -1 element
            max_l = -2 ** 31
            sum_l = 0
            for i in reversed(range(len(left))):
                sum_l += left[i]
                if sum_l > max_l:
                    max_l = sum_l
            # max subarray in right with left at 0 element
            max_r = -2 ** 31
            sum_r = 0
            for i in range(len(right)):
                sum_r += right[i]
                if sum_r > max_r:
                    max_r = sum_r
            # max subarray cross mid
            max_xmid = max_l + max_r
            return max([left_max_subarray, right_max_suvarray, max_xmid])
