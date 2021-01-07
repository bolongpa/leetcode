from heapq import *
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_k = len(nums) - k
        h = []
        for i in range(len(nums)):
            heappush(h, nums[i])
        i = 0
        while i < min_k + 1:
            out = heappop(h)
            print(out)
            if i == min_k:
                return out
            i += 1