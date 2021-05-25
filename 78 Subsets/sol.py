"""
If the array has only one item, there are two subsets: the empty set and the array itself. What if the array has two items?
We can generate all the subsets starting from the empty set, and then for every item in the array, we double the number of items in the results, by copying each subset and appending the current item to it.
nums = [1, 2]
[[]]
item = 1, subsets: [[], [1]]
item = 2, subsets: [[], [1], [2], [1, 2]]

O(N * 2^N) time and space
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for item in nums:
            result.extend([subset + [item] for subset in result])
        return result