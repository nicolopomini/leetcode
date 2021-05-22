"""
Rotating cells in groups of 4. We need to descend for the half of the rows (in case n is odd, the very final iteration would involve only the center cell, that stays where it is, so we can skip it)
We need to modify n / 2 columns (+1 in case n is odd), since the others will be modified in the first n / 2 rotations.
O(N^2) time, O(1) space
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n // 2 + n % 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        