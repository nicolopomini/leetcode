"""
We convert a char of the number to its unicode representation, shifting it back using the representation of the string '0'. In this way we can build an integer from the string
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def build_integer(string):
            total = 0
            mul_factor = 1
            for i in range(len(string) - 1, -1, -1):
                digit = ord(string[i]) - ord('0')
                total += digit * mul_factor
                mul_factor *= 10
            return total
        
        number_1 = build_integer(num1)
        number_2 = build_integer(num2)
        return str(number_1 * number_2)