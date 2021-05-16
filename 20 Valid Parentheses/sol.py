"""
Pretty easy, using a stack to see whether the last opened par matches the one we are closing.

O(N) time, O(N) space
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last_par = stack.pop()
                if c == ')' and last_par != '(':
                    return False
                if c == ']' and last_par != '[':
                    return False
                if c == '}' and last_par != '{':
                    return False
        if len(stack) > 0:
            return False
        return True