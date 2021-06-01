"""
We have to reach the end of the array in any of the available lines.
We can store the minimum number of jumps at every position, for every line.
jumps[i][l] is the min number of lateral jumps at position i in line l. The answer is jumps[0][1].

In case i == n - 1:
jumps[i][l] = 0 if obstacles[i] is not the current line, +inf otherwise
Otherwise:
we try first to stay on the same line, so at the beginning jumps[i][l] = jumps[i + 1][l] (if the current position is not an obstacle, otherwise +inf).
Then, we take the minimum between jumps[i][0], jumps[i][1], jumps[i][2]. For each position, if it is not +inf, we keep min(jumps[i][l], jumps[i][minrow]).
O(N) time, O(1) space since we need jumps[i] and jumps[i + 1] to compute all the sections.
"""
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        jumps = [0, 0, 0]
        for i in range(n - 1, -1, -1):
            current_jumps = [
                float('inf') if obstacles[i] == 1 else jumps[0],
                float('inf') if obstacles[i] == 2 else jumps[1],
                float('inf') if obstacles[i] == 3 else jumps[2],
            ]
            min_jumps = min(current_jumps)
            for j in range(3):
                if obstacles[i] != j + 1:
                    current_jumps[j] = min(current_jumps[j], min_jumps + 1)
            jumps = current_jumps
        return jumps[1]