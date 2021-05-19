"""
Use a boolean matrix matches[i][j] that tells if the string[i: ] matches with the pattern[j: ]
The answer will be in matches[0][0]

Base cases:
i == n and j == m: true, no more characters to examine
i == n => string is over, check if pattern can be skipped thanks to *
j == n => false, pattern is over and string is not: no match
otherwise need to differentiate between cases with star and without star:
- with star we can always try to advance the pattern, even if the characters don't match. If they do, we can advance on both string and pattern, or only on the string
- without start we compare the current character, and if they match we can continue.

O(NP) time and space, implemented using memoization
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def does_match(string, pattern, i, j, matches):
            # we implement memoization here
            if matches[i][j] is None:
                if i == len(string) and j == len(pattern):
                    matches[i][j] = True
                elif i == len(string):
                    if j < len(pattern) - 1 and pattern[j + 1] == '*':
                        # check if the rest of the pattern is skippable thanks to *
                        matches[i][j] = does_match(string, pattern, i, j + 2, matches)
                    else:
                        matches[i][j] = False
                elif j == len(pattern):
                    matches[i][j] = False
                else:
                    # comparing letters
                    has_star = j < len(pattern) - 1 and pattern[j + 1] == '*'
                    if has_star:
                        if string[i] == pattern[j] or pattern[j] == '.':
                            # 3 possibilities: 
                            # 1. Advance in both the string and the pattern
                            # 2. Advance only in the string
                            # 3. skip the char in the pattern and stay in the same position in the string
                            matches[i][j] = does_match(string, pattern, i + 1, j + 2, matches) or does_match(string, pattern, i + 1, j, matches) or does_match(string, pattern, i, j + 2, matches)
                        else:
                            # if the characters don't match, we can only try to skip the current char in the pattern using the *
                            matches[i][j] = does_match(string, pattern, i, j + 2, matches)
                    else:
                        # without the star, characters can only match
                        if pattern[j] == '.' or string[i] == pattern[j]:
                            matches[i][j] = does_match(string, pattern, i + 1, j + 1, matches)
                        else:
                            matches[i][j] = False
            return matches[i][j]
        
        matches = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return does_match(s, p, 0, 0, matches)