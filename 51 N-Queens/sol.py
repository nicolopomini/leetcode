"""
We have to place one queen per row.
We keep track of the already placed positions using a hashmap, containing tuples of coordinates (row, col)
We place one queen on one row, and we immediately pass on the second row.
To check whether the position is valid, we just need to check above us (vertically and diagonally).
In case we reach the n + 1 row, it means we found a valid positioning.
If at one point in time we have no places to place a queen into a row, some previous placement is wrong, and we need to backtrack.

Pseudocode:
- for each row:
	- check every column in the row, and if free, place a queen. Recurse to the next row
	- if no places available, return
	- if current row == n, we have a solution
	- finally, remove the placed queen and go on

Checking if a position is free:
- check column is easy;
- check upper left diagonal: row - col == other_row - other_col
- check upper right diagonal: row + col == other_row + other_col
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_free(row, col, queens):
            for q_row, q_col in queens:
                if q_col == col:
                    return False
                if q_row - q_col == row - col:
                    return False
                if q_row + q_col == row + col:
                    return False
            return True
        
        def add_result(queens, result, n):
            board = []
            for row in range(n):
                row_result = []
                for col in range(n):
                    if (row, col) in queens:
                        row_result.append('Q')
                    else:
                        row_result.append('.')
                board.append("".join(row_result))
            result.append(board)

        def get_solutions(n, row, queens, result):
            if row == n:
                add_result(queens, result, n)
                return
            for col in range(n):
                if is_free(row, col, queens):
                    queens.add((row, col))
                    get_solutions(n, row + 1, queens, result)
                    queens.remove((row, col))
        
        result = []
        get_solutions(n, 0, set(), result)
        return result