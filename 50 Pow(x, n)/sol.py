"""
What is a power? It's a repetition of multiplications.
10^4 = 10 * 10 * 10 * 10 = (10^2)^2
Base cases: exponenent is 0, return 1
exponent is 1, return the base.

If exponent is even, we can say that power(x, n) = pow(x, n // 2) * pow(x, n // 2)
otherwise, power(x, n) = pow(x, n // 2) * pow(x, n // 2) * x.

Negative powers: x^(-n) = 1/(x^n), just apply that
2^10 = 2^5 * 2^5 = 2^2 * 2^2 * 2 * 2^2 * 2^2 * 2.

O(log n) time and space, we are calling every time the same function once, passing the half of the exponent; therefore, it decreases exponentially towards 1, that is the base case. The space complexity is given by the recursive calls
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1.0
        if n == 1:
            return x
        is_even = n % 2 == 0
        half_power = self.myPow(x, n // 2)
        result = half_power * half_power
        return result if is_even else result * x