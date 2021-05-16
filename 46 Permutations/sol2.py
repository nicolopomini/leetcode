"""
Approach 2:
What are the permutations of [1, 2, 3]?
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
Basically, we can compute all the permutations of an array of length N by choosing the first item, and compute the permutations of the array of length N - 1. We can choose the first item as the first one in the permutations, compute all its permutations, and then swap it with all its successors, recursing, and then put it back to where it was.
Pseudocode.
For i in range(n):
    for j in range(i, n):
        swap item i with item j   # at the beginning we swap an item with itself, so nothing happens
        recurse considering the array from i + 1 to n
        swap item i with item j

O(N * N!) time and space
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def compute_permutations(array, index, results):
            if index == len(array):
                results.append(list(array))
            else:
                for i in range(index, len(array)):
                    array[index], array[i] = array[i], array[index]
                    compute_permutations(array, index + 1, results)
                    array[index], array[i] = array[i], array[index]

        results = []
        compute_permutations(nums, 0, results)
        return results