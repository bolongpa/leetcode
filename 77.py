class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        self.res = []

        def backtrack(nums_left, com=[]):
            if len(com) == k:
                self.res.append(com)
                return
            else:
                for i in range(len(nums_left)):
                    backtrack(nums_left[i + 1:], com + [nums_left[i]])
                return

        backtrack(nums)
        return self.res