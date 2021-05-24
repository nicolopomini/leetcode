"""
Double binary search: find the row first, and then the column.
O(log n + log m) time, O(1) space
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row = 0
        last_row = len(matrix) - 1
        row = None
        while first_row <= last_row:
            current_row = first_row + int((last_row - first_row) / 2)
            if matrix[current_row][0] <= target <= matrix[current_row][-1]:
                row = current_row
                break
            elif matrix[current_row][0] > target:
                last_row = current_row - 1
            else:
                first_row = current_row + 1
        if first_row > last_row:
            return False
        first_col = 0
        last_col = len(matrix[row]) - 1
        while first_col <= last_col:
            current_col = first_col + int((last_col - first_col) / 2)
            if matrix[row][current_col] == target:
                return True
            elif  matrix[row][current_col] > target:
                last_col = current_col - 1
            else:
                first_col = current_col + 1
        return False