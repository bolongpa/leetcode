class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # O(m+n)
        '''
        We choose the top-right corner as the start because we will have only one eligible walking direction after each check, the same for bottom-left corner. If we start from top-left or bottom-right, we encounter 2 possible directions and risk that index out of range
        '''
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False