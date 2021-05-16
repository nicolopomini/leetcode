"""
Approach 1:
Use two sets. At the beginning, first set empty and second full.
At every step remove one item from the second and put into the first, recurse
When the second is empty, the content of the first is a permutation
[] [1, 2, 3]
[1] [2, 3]
    [1, 2] [3]
        [1, 2, 3][]
    [1, 3] [2]
        [1, 3, 2]
[2] [1, 3]
    [2, 1][3]
        [2, 1, 3]
    [2, 3] [1]
        [2, 3, 1]
[3][1, 2]
    [3, 1] [2]
        [3, 1, 2]
    [3, 2] [1]
        [3, 2, 1]
N! permutations, each of length N. Space compl O(N * N!), Time compl O(N^2 * N!), because we remove and insert the item we are moving from the second to the first array, and it costs O(N).
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def compute_permutations(first, second, results):
            if len(second) == 0:
                results.append(list(first))
            else:
                for i in range(len(second)):
                    # move the item, preparing for the recursion
                    item = second.pop(i)
                    first.append(item)
                    compute_permutations(first, second, results)
                    # put back the item to its original place, for the next recursive steps
                    first.pop(-1)
                    second.insert(i, item)

        results = []
        compute_permutations([], nums, results)
        return results