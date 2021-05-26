"""
One approach is considering all the possible rectangles, checking if they only contain ones and compute their area. O(N^4) time, O(1) space.

We can use DP to make the algorithm faster. We can create a NxM matrix of integers, where each cell counts how many consecutive ones there are in the original matrix before the respective cell (the cell itself is included) on the same row.
[
 1 0 1 0 0
 1 0 1 1 1
 1 1 1 1 1
 1 0 0 1 0
]
we will have the following support matrix
[
 1 0 1 0 0
 1 0 1 2 3
 1 2 3 4 5
 1 0 0 1 0
]
Then, for every cell, we try to see how big the area of a rectangle with the upper right corner on that cell would be. To do so, we fix the starting column first, then we ieratate on all the rows to select the starting row, and we iterate again on all the rows greater or equal than the current row to select the last row. The height of the rectangle is given by the number of involved rows, and the width is given by the minimum value met on the starting column.
If N are the rows and M are the columns, O(N^2 * M) time, O(1) space
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        # first step, transform the matrix from strings to integers
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = int(matrix[row][col])
        
        # compute the consecutive ones on every row, directly on the input matrix
        for row in range(len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col] > 0:
                    matrix[row][col] += (matrix[row][col - 1])
        
        area = 0
        for right_column in range(len(matrix[0])):
            for start_row in range(len(matrix)):
                width = matrix[start_row][right_column]
                involved_rows = 1
                for end_row in range(start_row, len(matrix)):
                    width = min(width, matrix[end_row][right_column])
                    area = max(area, involved_rows * width)
                    involved_rows += 1
        return area