"""
The idea is the following: we need to decompose n into a sum of smaller numbers to maximize the product of such numbers, therefore we want to avoid using 1s as much as possible, 
and also we want to use the maximum achievable product of the numbers coming before n.
Given k < n, we can use the solution for (n - k) to compute the solution for n. How?
- we can use the solution for (n - k) and multiply it by k [e.g. n = 10, k = 3, so we can say that solution(10) = 3 * sol(7), where solution(7) is given by the product of 3 and 4]
- we can only multiply k * (n - k) [e.g. with n = 5, the best solution is given by 3 * 2, and not by 2 * solution(3) or 3 * solution(2)]

given n: the solution is:
max {k * solution(n - k), (n - k) * k} for all 2 <= k < n
Base cases: 1 => 1, 2 => 1

5:
    2 * sol(3) = 4
    2 * 3 = 5
    3 * sol(2) = 3
    3 * 2 = 5
    4 * sol(1) = 4
    4 * 1 = 4

O(N^2) time, O(n) space
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        max_products = []
        max_products.append(1) # 1
        max_products.append(1) # 2
        for i in range(3, n + 1):
            max_prod = 0
            for k in range(2, i):
                max_prod = max(max_prod, k * max_products[i - k - 1], k * (i - k))
            max_products.append(max_prod)
        return max_products[-1]