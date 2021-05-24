"""
M => the final matrix, at the beginning filled with zeros
start_row, end_row => the portion of the rows to be filled
start_col, end_col => the portion of the cols to be filled
Simply follow the logic: do the first row, the last column, the last row and the first column, and then restrict the start and end rows and cols.

O(N^2) time and space
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0 for _ in range(n)] for _ in range(n)]
        start_row, start_col = 0, 0
        end_row, end_col = n - 1, n - 1
        i, j = 0, 0
        counter = 1
        direction = 'right'
        for _ in range(n ** 2):
            M[i][j] = counter
            if direction == 'right':
                if j < end_col:
                    j += 1
                else:
                    start_row += 1
                    i += 1
                    direction = 'down'
            elif direction == 'down':
                if i < end_row:
                    i += 1
                else:
                    end_col -= 1
                    j -= 1
                    direction = 'left'
            elif direction == 'left':
                if j > start_col:
                    j -= 1
                else:
                    end_row -= 1
                    i -= 1
                    direction = 'up'
            else:
                if i > start_row:
                    i -= 1
                else:
                    start_col += 1
                    j += 1
                    direction = 'right'
            counter += 1
                    
        return M