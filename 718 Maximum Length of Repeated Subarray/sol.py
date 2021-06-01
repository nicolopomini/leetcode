"""
The subarray must be contiguous, so it cannot be like longest common substring, where "holes" are accepted.
We have to find the longest common prefix (or suffix) in the two arrays.
If one of the two are empty (the index is beyond the last item) the lenght of the longest common subarray is 0.
If the items pointed by the two pointers are the same, the longest subarray is 1 + the longest subarray in i + 1, j + 1. If the latter is 0, it means that nums1[i + 1] and nums2[j + 1] are different, and therefore the subarray ends there.
We need to return the maximum of these lengths.
O(N * M) time and space
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        longest = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        longest_subsequence = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    longest[i][j] = 1 + longest[i + 1][j + 1]
                    longest_subsequence = max(longest_subsequence, longest[i][j])

        return longest_subsequence