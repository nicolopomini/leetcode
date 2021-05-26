"""
DP with a 4D matrix [start1, end1, start2, end2]
We compare substrings of the same length (otherwise they are not scrambled), and they have to contain the same characters and the same number of them.
In case they do, try all the possible splits of the two strings and recurse.

Let N be the length of s1, M be the length of s2, O(N^2 * M^2) time and space
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def check_scramble(s1, s2, start1, end1, start2, end2, dp):
            if dp[start1][end1][start2][end2] is None:
                # basic checks
                if end1 - start1 != end2 - start2:
                    dp[start1][end1][start2][end2] = False
                elif s1[start1: end1] == s2[start2: end2]:
                    dp[start1][end1][start2][end2] = True
                else:
                    counts = {x: 0 for x in s1[start1: end1] + s2[start2: end2]}
                    for c in s1[start1: end1]:
                        counts[c] += 1
                    for c in s2[start2: end2]:
                        counts[c] -= 1
                    result = True
                    for c in counts.values():
                        if c != 0:
                            result = False
                    if not result:
                        dp[start1][end1][start2][end2] = False
                    else:
                        dp[start1][end1][start2][end2] = False
                        for i in range(1, end1 - start1):
                            # checking split at index i
                            if check_scramble(s1, s2, start1, start1 + i, start2, start2 + i, dp) and check_scramble(s1, s2, start1 + i, end1, start2 + i, end2, dp):
                                dp[start1][end1][start2][end2] = True
                                break
                            if check_scramble(s1, s2, start1, start1 + i, end2 - i, end2, dp) and check_scramble(s1, s2, start1 + i, end1, start2, end2 - i, dp):
                                dp[start1][end1][start2][end2] = True
                                break
            return dp[start1][end1][start2][end2]
        
        dp = [[[[None for _ in range(len(s2) + 1)] for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)] for _ in range(len(s1) + 1)]
        return check_scramble(s1, s2, 0, len(s1), 0, len(s2), dp)
