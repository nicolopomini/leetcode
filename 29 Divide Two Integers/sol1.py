"""
Just apply the division as it is: a series of repeated subtractions.
We check the sign first and then we operate with positive numbers.

O(dividend / divisor) time, O(1) space
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            return sign * dividend if -2 ** 31 <= sign * dividend <= 2 ** 31 - 1 else 2 ** 31 - 1
        result = 0
        accumulator = divisor
        while accumulator <= dividend:
            accumulator += divisor
            result += 1
        result *= sign
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        return 2 ** 31 - 1