class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i in matrix:
            if target == i[0]:
                res = True
            elif target <= i[-1]:
                for j in i:
                    if j == target:
                        res = True
        return res