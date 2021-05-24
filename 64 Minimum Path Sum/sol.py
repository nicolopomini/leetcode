"""
Very similar to the previous problem: at every position we want to choose the neighbour with the minimum value.
Also in this case we could use the input matrix to keep track of the values.

O(N*M) time and space
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        M = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if row == m - 1 and column == n - 1:
                    M[row][column] = grid[row][column]
                elif row + 1 < m and column + 1 < n:
                    M[row][column] = grid[row][column] + min(M[row + 1][column], M[row][column + 1])
                elif row + 1 < m:
                    M[row][column] =grid[row][column] + M[row + 1][column]
                else:
                    M[row][column] =grid[row][column] + M[row][column + 1]
        return M[0][0]