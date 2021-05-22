"""
Better approach, we try to double up the divisor after every division (in the inner loop), to try to reduce the number of iterations. We keep track of the number of times the divisor has been doubled in the `multiplied_by` variable. If we go too far, the outer loop will reset the multiplied_by, to start again from the last good divisor we found

O(log (dividend / divisor)) time, O(1) space
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            current_divisor = divisor
            multiplied_by = 1
            while dividend >= current_divisor:
                result += multiplied_by
                dividend -= current_divisor
                multiplied_by += multiplied_by
                current_divisor += current_divisor
        result *= sign
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        return 2 ** 31 - 1