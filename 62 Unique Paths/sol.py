"""
if [i, j] is the end, or has only one direction to go, there is only 1 path
otherwise sum of the number of paths available from their two neighbours (right or down)

matrix M containing the number of available paths in any position
start bottom right to compute them, and go back until [0,0]
result is in [0,0]

O(N*M) time and space
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if row + 1 < m and column + 1 < n:
                    M[row][column] = M[row + 1][column] + M[row][column + 1]
                else:
                    M[row][column] = 1
        return M[0][0]