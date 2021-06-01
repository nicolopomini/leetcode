"""
- Every player has to pick at least 2 stones
- Every player wants to maximize its score and minimize the other's.

Let score[i] be the maximum score difference that the current player can get when the first stone is at index i. The answer will be score[0].
If i == N - 2, we have to take all the stones, score[i] = stones[n - 2: ]
otherwise, we can try taking any number of stones, from i to n - 1. Let's say that we choose to use stones until j (excluded). So score[i] = sum(stones[i: j]) - score[j], since score[j] will be the best score of the other player.
We have to take the j that maximizes the difference.
In order to make things more efficient, we can precompute the sums of stones in the main array. Stones[i] += stones[i - 1], for all i from 1 to n - 1.
Score[i] = stones[j] + score[j], for i < j < N - 2
score[n - 2] = stones[-1] 
We compute the scores from n - 2 to 0, so for example: 
score[3] = max(stones[4] - score[4], stones[5] - score[5], stones[6] - score[6], etc)
score[2] = max(stones[3] - score[3], stones[4] - score[4], stones[5] - score[5], etc) = max(stones[3] - score[3], score[3])
so we can do it in linear time, and store only one value for the score.
O(N) time O(1) space.
"""
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        # precompute the sum of the stones
        for i in range(1, n):
            stones[i] += stones[i - 1]
        score = stones[-1]
        for i in range(n - 2, 0, -1):
            # we end at 1 because we have to choose at least two stones
            score = max(score, stones[i] - score)
        return score