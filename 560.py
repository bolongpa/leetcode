class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicts = {0: 1}
        count = 0
        s = 0
        for i in nums:
            s += i
            if s - k in dicts:
                count += dicts[s - k]
            if s in dicts:
                dicts[s] += 1
            else:
                dicts[s] = 1
        return count
