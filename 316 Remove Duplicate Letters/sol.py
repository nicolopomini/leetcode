"""
Approach #1: create a set with the letters, and return a sorted list created by the set.
O(N logN) time, O(N) space

Approach #2: we need to count how many times a single characters appear.
Then we use a stack to build the solution: for each char in string, we check if:
- the stack is not empty
- if the top of the stack is greater than the current char
- if the counter of the char at the top of the stack is > 0
If all the 3 things are true, we can remove the char at the top of the stack. Since there are other instances of it left after here, we will add it later.

O(N) time and space
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counters = {}
        for c in s:
            if c not in counters:
                counters[c] = 0
            counters[c] += 1
        visited = {c: False for c in s}
        stack = []
        for c in s:
            counters[c] -= 1
            if visited[c]:
                continue
            while stack and stack[-1] > c and counters[stack[-1]] > 0:
                popped = stack.pop()
                visited[popped] = False
            stack.append(c)
            visited[c] = True
        return "".join(stack)