class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming, O(n^2)
        l = len(s)
        # initialize dynamic programming table
        dp_matrix = [[0] * l for i in range(l)]
        for i in range(l):
            dp_matrix[i][i] = 1
        longest = 1
        max_left_id = max_right_id = 0

        for i in range(l):
            right = i
            left = 0
            for left in range(right):
                if right > left + 1:
                    dp_matrix[left][right] = dp_matrix[left + 1][right - 1] * s[right] == s[left]
                else:
                    dp_matrix[left][right] = s[right] == s[left]
                if dp_matrix[left][right] and right - left + 1 > longest:
                    longest = right - left + 1
                    max_left_id, max_right_id = left, right

        return s[max_left_id:max_right_id + 1]

'''
with using Manacher's Algorithm we can solve with complexity of O(n)
# 98.8%;58.2%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # COPIED FROM SOME OTHER USER
        if len(s)==1 or s==s[::-1]: return s
        a,b = 0,1  # b is the length of palindromic substring
        for i in range(1, len(s)):
            if i-b-1>=0 and s[i-b-1:i+1] == s[i-b-1:i+1][::-1]:
                a = i-b-1
                b += 2
                continue
            if s[i-b:i+1] == s[i-b:i+1][::-1]:
                a = i-b
                b += 1
        return s[a:a+b]
'''