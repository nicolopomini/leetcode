"""
We cannot just count the characters and see the differences, because the order with which they appear matters.
We use dynamic programmin to solve this problem. Let deletions[i][j] a matrix, where cell [i, j] contains the minimum number of steps to solve the problem of word1[i:] and word2[j:].
i == len(word1) and j == len(word2) => 0
i == len(word1) => len(word2) - j
j == len(word2) => len(word1) - i
word1[i] == word2[j] => deletions[i + 1][j + 1]
otherwise => 1 + min(deletions[i + 1][j], deletions[i][j + 1]).

O(NM) time, O(NM) space
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def compute_min_deletions(word1, word2, i, j, deletions):
            if deletions[i][j] is None:
                if i == len(word1) and j == len(word2):
                    deletions[i][j] = 0
                elif i == len(word1):
                    deletions[i][j] = len(word2) - j
                elif j == len(word2):
                    deletions[i][j] = len(word1) - i
                elif word1[i] == word2[j]:
                    deletions[i][j] = compute_min_deletions(word1, word2, i + 1, j + 1, deletions)
                else:
                    deletions[i][j] = 1 + min(compute_min_deletions(word1, word2, i, j + 1, deletions), compute_min_deletions(word1, word2, i + 1, j, deletions))
            return deletions[i][j]
        
        deletions = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        return compute_min_deletions(word1, word2, 0, 0, deletions)
        