"""
We must split nums into k groups.
Every group has at least one element, and it is made by adjacent elements.
If we have to create at most k groups.
let best_avg[index][k] a matrix containing the best average of k groups of nums[i: ]. The answer of the problem is best_avg[0][k].
Base case: k = 1, the answer is the avg of the numbers in nums[i:]
Otherwise, we have to try all the possibilities:
from the current index, try to create a group of 1 element and recurse, then a group of 2 elements and recurse, keep doing so until the index is <= len(nums) - k. Choose the one that maximizes the result. We are not forced to split in k parts, we can use even less than k splits

Since the recursive formula uses only the previous k, we can build the dynamic programming matrix bottom up, using only O(N) space. Another optimization is creating an array sums, where sums[i] is the sum of nums[:i included]. This allows us to compute all the avg in constant time

O(N^2 * k) time, O(N) space
"""

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        # at the beginning, no splits. The best we can get is the avg of nums[i:]
        best_avg = [(sums[-1] - sums[i]) / (len(nums) - i) for i in range(len(nums))]
        # we split in group groups, from 2 to k inclusive
        for groups in range(2, k + 1):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    # i is the start of the group, j is the end (exclusive)
                    best_avg[i] = max(best_avg[i], best_avg[j] + (sums[j] - sums[i]) / (j - i))
        return best_avg[0]
            