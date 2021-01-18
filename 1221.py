class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) == 1:
            return 0
        stack = []
        stack.append(s[0])
        s = s[1:]
        cnt = 0
        while s:
            curr = s[0]
            s = s[1:]
            if not stack:
                stack.append(curr)
            else:
                if curr != stack[-1]:
                    del stack[-1]
                    if not stack:
                        cnt += 1
                else:
                    stack.append(curr)
        return cnt
