class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        if n <= 1:
            return 1
        else:  # n >= 2
            dp_dict = {}
            dp_dict[0] = 1
            dp_dict[1] = 1
            for i in range(2, n+1):
                dp_dict[i] = dp_dict[i-1] + dp_dict[i-2]
            return dp_dict[n]
