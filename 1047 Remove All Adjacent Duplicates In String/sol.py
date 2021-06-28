"""
We can use a stack to process the word:
- if the stack is empty or the top of the stack is different from the current letter, push the current letter on the stack
- otherwise, remove the top of the stack and ignore the current letter
What is left in the stack is the result.
O(N) time and space
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)