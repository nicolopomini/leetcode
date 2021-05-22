"""
Solved using a stack.
At the beginning the stack contains the index before the beginning of the current valid substring. So at the beginning the substring will start from 0, and therefore the stack will have -1 as initial value.
Every time we face an open parenthesis, we push its index to the top of the stack.
Every time we face a close parenthesis, we pop from the stack (removing the index that was matching with the parenthesis). Now two things can happen:
- the stack is empty, meaning that the close parenthesis we just met did not have any matching open parenthesis. In this case, we push the current index to the top of the stack, that will represent the index before the beginning of the next valid substring
- if the stack is not empty, we read the top of the stack and we compute the difference with the close parenthesis we met: that's the length of the valid substring closed by the parenthesis.

O(N) time and space
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack) > 0:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len