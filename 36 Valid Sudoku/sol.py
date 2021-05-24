"""
To check whether the sudoku is valid, just check all the rows, the columns and the 9 3x3 cells.

O(1) time and space, since the size of the board is constant
"""
class Solution:
    def isValid(self, cells: List[str]) -> bool:
        number_count = 0
        number_set = set()
        for cell in cells:
            if cell != '.':
                number_count += 1
                number_set.add(cell)
        return len(number_set) == number_count
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in board:
            if not self.isValid(row):
                return False
        # validate columns
        for col in range(9):
            column = [r[col] for r in board]
            if not self.isValid(column):
                return False
        # validate sub-cell
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                cell = []
                for i in range(3):
                    cell.extend(board[start_row + i][start_col: start_col + 3])
                if not self.isValid(cell):
                    return False
        return True
            