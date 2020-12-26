class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalpha() or c.isdigit())
        s = s.lower()
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True
