"""
Scan the matrix and set the original 0s to None, in this way we know which cells were at 0 in the original matrix
Rescan the matrix, and set to 0 all the rows and columns containing a None, keeping None as None
Finally, rescan the matrix and set all None to 0.

O(nm) time, O(1) space 
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    # put to 0 all row i
                    for col in range(m):
                        matrix[i][col] = 0 if matrix[i][col] is not None else None
                    # put 0 to col j
                    for row in range(n):
                        matrix[row][j] = 0 if matrix[row][j] is not None else None
        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        