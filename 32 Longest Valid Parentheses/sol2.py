"""
Use two counters: one for the open parenthesis and one for the close ones.
When we face an open parenthesis, we increment the open counter, when we face a close parenthesis we increment the close counter. If close > open, we reset the counters, it is not possible to obtain a valid substring with what came before, if close == open, we have a valid substring.
Then we repeat the operation traversin the string right to left (the cases are symmetrical).

O(N) time, O(1) space
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def find_longest_valid_par(string, reverse):
            opened = 0
            closed = 0
            max_len = 0
            loop = range(len(s)) if not reverse else range(len(s) - 1, -1, -1)
            for i in loop:
                if string[i] == '(':
                    opened += 1
                else:
                    closed += 1
                if opened == closed:
                    max_len = max(max_len, opened * 2)
                elif closed > opened and not reverse:
                    opened = 0
                    closed = 0
                elif opened > closed and reverse:
                    opened = 0
                    closed = 0
            return max_len
        
        return max(find_longest_valid_par(s, False), find_longest_valid_par(s, True))
        