"""
Plus and minus signs, and parenthesis. Spaces must be ignored, so '1+-1' is equal to 0
If there were not parenthesis, it would be straightforward.
We have to reduce parenthesis to single numbers, respecting their cascading. We also need to consider the sign before the parenthesis.

We can use a stack, traversing the string right to left and pushing items on the stack.
When we face an open parenthesis, we pop all the elements until the closing one, and we evaluate the parenthesis
When we push a digit, we push it multiplying it by its correspective power of 10, based on where it was seen
O(N) time and space
"""
class Solution:
    def calculate(self, s: str) -> int:
        def is_digit(char):
            return '0' <= char <= '9'
        
        def evaluate_par(stack):
            res = 0
            while stack and stack[-1] != ')':
                is_plus_sign = True
                # there can be multiple signs one after the other, and even at the beginning of the stack
                while not isinstance(stack[-1], int):
                    sign = stack.pop()
                    if sign == '-':
                        is_plus_sign = not is_plus_sign
                # once the sign is handled, we are sure to get a number
                if is_plus_sign:
                    res += stack.pop()
                else:
                    res -= stack.pop()
            return res
        
        stack = []
        digit = 0
        operand = 0
        for char in reversed(s):
            if is_digit(char):
                operand += int(char) * 10 ** digit
                digit += 1
            else:
                if digit > 0:
                    stack.append(operand)
                    operand = 0
                    digit = 0
                if char == '(':
                    parenthesis_result = evaluate_par(stack)
                    stack.pop()
                    stack.append(parenthesis_result)
                elif char != ' ':
                    stack.append(char)
        if digit > 0:
            stack.append(operand)
        return evaluate_par(stack)