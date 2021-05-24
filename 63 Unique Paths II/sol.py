"""
Similar to the previous problem, for each position we compute the number of paths available to reach the bottom right corner. Of course if the cell contains an obstacle, its paths are 0.
For all the other cells I need to check if at least one of the two neighbour has at least 1 path, otherwise also from that cell is not possible to reach the goal.

O(N*M) time and space (we could actually modify the input and use it as matrix to keep the paths, in that case space would be O(1))
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        M = [[0 for _ in range(columns)] for _ in range(rows)]
        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                if obstacleGrid[row][column] == 1:
                    M[row][column] = 0
                elif row == rows -1 and column == columns - 1:
                    M[row][column] = 1
                elif row + 1 < rows and column + 1 < columns:
                    M[row][column] = M[row + 1][column] + M[row][column + 1]
                elif row + 1 < rows:
                    M[row][column] = M[row + 1][column]
                else:
                    M[row][column] = M[row][column + 1]
        return M[0][0]