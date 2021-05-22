"""
if I finished both strings at the same time => True
if I finished only one string => False
if I meet '?', andvance both the pointers
If I meet '*', try to advance only the pointer in the pattern (skip char) of only the pointer in the string

M[i, j] tells whether the string starting at i matches with pattern starting at j
answer is M[0, 0]
in general, they match if s[i] == p[j] and the rest of the string and pattern match too
O(N*M) time and space
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def does_match(s: str, p: str, i: int, j: int, match):
            if match[i][j] is None:
                if i == len(s) and j == len(p):
                    match[i][j] = True
                elif i < len(s) and j == len(p):
                    match[i][j] = False
                elif i == len(s) and j < len(p):
                    match[i][j] = does_match(s, p, i, j + 1, match) if p[j] == '*' else False
                elif s[i] == p[j] or p[j] == '?':
                    match[i][j] = does_match(s, p, i + 1, j + 1, match)
                elif p[j] == '*':
                    match[i][j] = does_match(s, p, i, j + 1, match) or does_match(s, p, i + 1, j, match)
                else:
                    match[i][j] = False
            return match[i][j]
            
        match = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        does_match(s, p, 0, 0, match)
        return match[0][0]