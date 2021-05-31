"""
We use dynamic programming, defining longest[i, j] the length of the longest fibonacci subsequence starting with elements i and j of the array. The next element will be the one having an item = array[i] + array[j], let's call it z
and so longest[j, z] = longest[i, j] + 1. While we compute all the subsequences, we keep track of the longest we have found.
We create a hashmap to find in constant time the index of a given element, if it exists.
O(N^2) time and space
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indexes = {arr[i]: i for i in range(len(arr))}
        longest = [[2 for _ in range(len(arr))] for _ in range(len(arr))]
        answer = 0
        for first_index in range(len(arr) - 2):
            for second_index in range(first_index + 1, len(arr) - 1):
                third_index = indexes.get(arr[first_index] + arr[second_index], -1)
                if third_index > second_index:
                    longest[second_index][third_index] = longest[first_index][second_index] + 1
                    answer = max(answer, longest[second_index][third_index])
        return answer if answer >= 3 else 0