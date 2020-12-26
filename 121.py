from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxm = 0
        while j < len(prices):
            profit = prices[j]-prices[i]
            if profit >= maxm:
                j = j+1
                maxm = profit
            elif profit <= 0:  # update the min position no bigger than the poiter seeking max
                i = j
                j = j+1
            elif 0 < profit < maxm:
                j = j+1
        return maxm