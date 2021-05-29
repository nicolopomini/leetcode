"""
Build a NxN support matrix, where each element contains 4 items [up, left, down, right], indicating how many consecutive ones there are above the current cell (cell included) how many consecutive ones there are on the left (cell included), how many consecutive ones there are below and how many consecutive ones there are on the right (cell included)
n = 5, mines = [[4, 2]] (considering only above and left in this example)
[1,1], [1,2], [1,3], [1,4], [1,5],
[2,1], [2,2], [2,3], [2,4], [2,5],
[3,1], [3,2], [3,3], [3,4], [3,5],
[4,1], [4,2], [4,3], [4,4], [4,5],
[5,1], [5,2], [0,0], [5,1], [5,2]
Then we consider every cell as the center of the plus sign, and the max order we can reach from there is the minimum between the 4 numbers.
Return the maximum of every minimum.
O(N^2) time and space
"""
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        counters = [[[] for _ in range(n)] for _ in range(n)]
        holes = set([(row, col) for row, col in mines])
        # left counters
        for row in range(n):
            for col in range(n):
                if (row, col) in holes:
                    counters[row][col].append(0)
                elif col == 0:
                    counters[row][col].append(1)
                else:
                    counters[row][col].append(1 + counters[row][col - 1][0])
        # right counters
        for row in range(n):
            for col in range(n - 1, -1, -1):
                if (row, col) in holes:
                    counters[row][col].append(0)
                elif col == n - 1:
                    counters[row][col].append(1)
                else:
                    counters[row][col].append(1 + counters[row][col + 1][1])
        # above counters
        for row in range(n):
            for col in range(n):
                if (row, col) in holes:
                    counters[row][col].append(0)
                elif row == 0:
                    counters[row][col].append(1)
                else:
                    counters[row][col].append(1 + counters[row - 1][col][2])
        # below counters
        for row in range(n - 1, -1, -1):
            for col in range(n):
                if (row, col) in holes:
                    counters[row][col].append(0)
                elif row == n - 1:
                    counters[row][col].append(1)
                else:
                    counters[row][col].append(1 + counters[row + 1][col][3])
        answer = 0
        for row in range(n):
            for col in range(n):
                answer = max(answer, min(counters[row][col]))
        return answer