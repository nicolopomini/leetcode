"""
Non negative numbers, 4 basic operations, truncated division
Of course multiplication and division has the priority
We can use a stack to store the single numbers that will be summed at the end: if the operation is -, we can push the negated next number
If the operation is a multiplication or a division, we have to compute it and then push on the stack
O(N) time and space
"""
class Solution:
    def calculate(self, s: str) -> int:
        def is_digit(char):
            return '0' <= char <= '9'
        
        stack = []
        operation = '+'
        current_number = 0
        for i, char in enumerate(s):
            if is_digit(char):
                current_number = (current_number * 10) + int(char)
            if (not is_digit(char) and char != ' ') or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                else:
                    stack.append(int(stack.pop() / current_number))
                operation = char
                current_number = 0
        return sum(stack)