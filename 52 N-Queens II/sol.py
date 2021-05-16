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
    def totalNQueens(self, n: int) -> int:
        def is_free(row, col, queens):
            for q_row, q_col in queens:
                if q_col == col:
                    return False
                if q_row - q_col == row - col:
                    return False
                if q_row + q_col == row + col:
                    return False
            return True

        def get_number_of_solutions(n, row, queens):
            if row == n:
                return 1
            number_of_solutions = 0
            for col in range(n):
                if is_free(row, col, queens):
                    queens.add((row, col))
                    number_of_solutions += get_number_of_solutions(n, row + 1, queens)
                    queens.remove((row, col))
            return number_of_solutions
        
        return get_number_of_solutions(n, 0, set())
