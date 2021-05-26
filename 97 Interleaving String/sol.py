"""
We use DP with a 2D array to solve this problem.
Memo[i][j] tells us whether s1[i:] and s2[j:] are interleaving in s3[i + j:]
if i or j are at the end of s1 or s2, we have to check if the remaining part of the string is equal to what is left
Otherwise: 
If the two characters are the same, we have to advance both i and j in two separate cases
If the s1 character matches the character in s3, advance i
If the s2 character matches the character in s3, advance j
otherwise the two partial strings are not interleaving

O(NM) time and space
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def are_interleaving(s1, s2, s3, i, j, k, memo):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if memo[i][j] is None:
                memo[i][j] = False
                if s3[k] == s1[i] and s3[k] == s2[j]:
                    memo[i][j] = are_interleaving(s1, s2, s3, i + 1, j, k + 1, memo) or are_interleaving(s1, s2, s3, i, j + 1, k + 1, memo)
                elif s3[k] == s1[i]:
                    memo[i][j] = are_interleaving(s1, s2, s3, i + 1, j, k + 1, memo)
                elif s3[k] == s2[j]:
                    memo[i][j] = are_interleaving(s1, s2, s3, i, j + 1, k + 1, memo)
            return memo[i][j]
        
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        return are_interleaving(s1, s2, s3, 0, 0, 0, memo)