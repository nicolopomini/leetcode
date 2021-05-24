"""
M[i, j] indicating the min numb. of operation to transform word1[i: ] into word2[i: ]
result is in M[0, 0]

base case:
if i == len(word1) and j == len(word2): 0
elif i == len(word1): len(word2) - j
elif j == len(word2): len(word1) - i

Solved using memoization.
O(word1 * word2) time and space
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def computeMinDistance(word1, word2, i, j, distances):
            if distances[i][j] is None:
                if i == len(word1) and j == len(word2):
                    distances[i][j] = 0
                elif i == len(word1):
                    distances[i][j] = len(word2) - j
                elif j == len(word2):
                    distances[i][j] = len(word1) - i
                elif word1[i] == word2[j]:
                    distances[i][j] = computeMinDistance(word1, word2, i + 1, j + 1, distances)
                else:
                    distances[i][j] = 1 + min(computeMinDistance(word1, word2, i + 1, j + 1, distances),
                                             computeMinDistance(word1, word2, i + 1, j, distances),
                                             computeMinDistance(word1, word2, i, j + 1, distances))
            return distances[i][j]
        
        distances = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        return computeMinDistance(word1, word2, 0, 0, distances)
        