class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            left = right = 0
            max_str = 0
            while right < len(s):
                string = s[left:right]
                if s[right] not in string:
                    string += s[right]
                    max_str = max(len(string), max_str)
                    right += 1
                elif left <= right:
                    left += 1
                else:
                    right += 1
                print(string)
            return max_str
