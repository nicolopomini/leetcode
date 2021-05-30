"""
The greedy approach of choosing the path giving the most number of cherries, modifying the input grid and then choosing the backwards path in a greedy way again does not work. That is because the input grid changes.
The solution is too complicated for me, I just followed the best answer https://leetcode.com/problems/cherry-pickup/discuss/109903/Step-by-step-guidance-of-the-O(N3)-time-and-O(N2)-space-solution and the solution proposed by leetcode
In a nutshell, we can reverse the secondo path, and instead of going downwards and backwards, we can have two paths going from 0, 0 to n - 1, n - 1 simultaneously.
At every step, the two paths will have the same distance from 0,0; so we can recognize them by 3 variables row1, col1, col2. Since row1 + col1 = row2 + col2, we have row2 = row1 + col1 - col2. If grid[row1][col1] and grid[row2][col2] are not thorns, the result is grid[row1][col1] + grid[row2][col2] + max of (path1 goes down and path2 goes down, path1 goes down and path2 goes right, path1 goes right and path2 goes down, path1 goes right and path2 goes right). We have to be careful in not duplicate the case in which row1 = row2 and col1 = col2

O(N^3) time and space
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def most_picked_cherries(row1, col1, col2, grid, memo):
            n = len(grid)
            row2 = row1 + col1 - col2
            if row1 == n or row2 == n or col1 == n or col2 == n:
                # out of bounds
                return float('-inf')
            if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                # thorns found
                return float('-inf')
            if col1 == n - 1 and row1 == n - 1:
                # arrived to destination
                return grid[row1][col1]
            if memo[row1][col1][col2] is None:
                memo[row1][col1][col2] = grid[row1][col1]
                if col1 != col2:
                    # avoid duplicates
                    memo[row1][col1][col2] += grid[row2][col2]
                memo[row1][col1][col2] += max(most_picked_cherries(row1, col1 + 1, col2 + 1, grid, memo), most_picked_cherries(row1, col1 + 1, col2, grid, memo), most_picked_cherries(row1 + 1, col1, col2 + 1, grid, memo), most_picked_cherries(row1 + 1, col1, col2, grid, memo))
                
            return memo[row1][col1][col2]
        
        n = len(grid)
        memo = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return max(0, most_picked_cherries(0, 0, 0, grid, memo))