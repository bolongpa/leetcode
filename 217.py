from typing import List


# hash table
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash to hashtable
        hashtable = {k: [] for k in range(17)}
        for i in nums:
            if i in hashtable[i % 17]:
                return True
                # break
            else:
                hashtable[i % 17].append(i)
        return False


# sorting
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         if len(nums) > 1:
#             for i in range(len(nums)-1):
#                 if nums[i] == nums[i+1]:
#                     return True
#         return False

# internal func
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)
