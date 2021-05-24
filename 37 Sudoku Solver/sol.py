"""
For each empty cell, create a set of candidate numbers to be put in.
The solve function modifies the input, placing numbers on the board. If we reach a point in which there are empty cells to be empty but no value can fit in, it returns False and the algorithm backtracks, removing what was placed before.
If we reach the end of the board with all the cells filled, we found the solution!

Since the size of the board is fixed, O(1) time and space
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_candidates_row(board, row):
            already_used = set()
            for item in board[row]:
                already_used.add(item)
            return already_used
        
        def get_candidates_col(board, col):
            already_used = set()
            for row in range(len(board)):
                already_used.add(board[row][col])
            return already_used
        
        def get_candidates_cell(board, row, col):
            already_used = set()
            i = int(row / 3)
            j = int(col / 3)
            for x in range(3 * i, 3 * (i + 1)):
                for y in range(3 * j, 3 * (j + 1)):
                    already_used.add(board[x][y])
            return already_used
        
        def get_candidates(board, row, col):
            candidates = set([str(i) for i in range(1, 10)])
            candidates -= get_candidates_row(board, row)
            candidates -= get_candidates_col(board, col)
            candidates -= get_candidates_cell(board, row, col)
            return candidates
        
        def solve(board, row, col):
            if col == len(board):
                col = 0
                row += 1
                if row == len(board):
                    return True
            if board[row][col] != '.':
                return solve(board, row, col + 1)
            candidates = get_candidates(board, row, col)
            for candidate in candidates:
                board[row][col] = candidate
                if solve(board, row, col + 1):
                    return True
            board[row][col] = '.'
            return False
        
        solve(board, 0, 0)
        