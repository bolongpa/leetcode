class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n

        res = 0
        for i in range(m):
            stack = []
            prev, nex = [-1] * n, [n] * n
            for j in range(n):
                dp[j] = (matrix[i][j] == '1') * (dp[j] + 1)
                while stack and dp[stack[-1]] >= dp[j]:
                    nex[stack.pop()] = j
                if stack:
                    prev[j] = stack[-1]
                stack.append(j)
            for j in range(n):
                res = max(res, (nex[j] - prev[j] - 1) * dp[j])

        return res