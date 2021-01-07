class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(permutation=[]):
            if len(permutation) == len_nums:
                self.answer.append(permutation)
                return
            else:
                for num in nums:
                    if num not in permutation:
                        backtrack(permutation + [num])
                return

        len_nums = len(nums)
        self.answer = []
        backtrack()
        return self.answer