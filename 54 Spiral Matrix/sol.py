"""
The matrix is m x n, so we need to keep track of the first and last row, and first and last column to be visited at each iteration.
Every loop will start from the upper left corner, will push elements into the result array and then the limits will be updated.
O(N*M) time and space
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = 0
        end_row = len(matrix) - 1
        start_col = 0
        end_col = len(matrix[0]) - 1
        result = []
        while start_row <= end_row and start_col <= end_col:
            # upper row
            for col in range(start_col, end_col + 1):
                result.append(matrix[start_row][col])
            start_row += 1
            if start_row > end_row:
                break
            # right col
            for row in range(start_row, end_row + 1):
                result.append(matrix[row][end_col])
            end_col -= 1
            if start_col > end_col:
                break
            for col in range(end_col, start_col - 1, -1):
                result.append(matrix[end_row][col])
            end_row -= 1
            if start_row > end_row:
                break
            for row in range(end_row, start_row - 1, -1):
                result.append(matrix[row][start_col])
            start_col += 1
        return result