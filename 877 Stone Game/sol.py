"""
At least two piles, we need to return true if the first player wins the game, false otherwise.
The winner is the one throwing more stones.
Base case: only one pile, pick from it.
General case: we use a matrix indicating the difference between the stones thrown by the first player and the second.
Since we want to maximize our score, but also the other player plays always optimally, we take the maximum between picking from left and subtracting the best score of the opponent, or picking from right and subtrack the best score of the opponent in that case
The first player wins the difference is > 0

O(N^2) time and space.

Note that since the piles are even and the first player always starts first, he can always pick the even or the odd pile, and so we could decide which to pick taking the largest sum between the odd piles and the even piles, so the result is always true
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        score_differences = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            score_differences[i][i] = piles[i]
        for pile_size in range(2, n + 1):
            for left_index in range(n - pile_size + 1):
                right_index = left_index + pile_size - 1
                score_differences[left_index][right_index] = max(
                    piles[left_index] - score_differences[left_index + 1][right_index],
                    piles[right_index] - score_differences[left_index][right_index - 1]
                )
        return score_differences[0][n - 1] > 0
                