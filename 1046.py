from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            heapq._heapify_max(stones)
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if x != y:
                new = y - x
                heapq.heappush(stones, new)
        if stones:
            return stones[0]
        else:
            return 0
