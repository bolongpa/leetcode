from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = deque()
        for i in path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if not stack:  # stack is empty
                    continue
                else:
                    stack.pop()
            else:
                stack.append(i)

        # output
        if not stack:
            return '/'
        else:
            return '/' + '/'.join([i for i in stack])
