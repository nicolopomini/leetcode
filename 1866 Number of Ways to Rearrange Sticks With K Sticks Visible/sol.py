"""
N sticks numbered from 1 to N (so they are unique).
Find all the permutations such that exactly k sticks have no higher sticks on their left.
The easiest way to do it is by placing the rightmost stick first:
- if we choose the highest stick, it will be visible, and so we are left with n - 1 sticks to place and k - 1 stick to see. (in other words, sticks[n][k] = sticks[n - 1][k - 1])
- otherwise, we have n - 1 choices to place a stick that is not the highest, and we are left with n - 1 sticks to place and k sticks to see. (sticks[n][k] = (n - 1) * sticks[n - 1][k])

Base cases:
k == n, the result is 1
k == 0, the result is 0

Overall, O(nk) time and space
"""
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        def place_sticks(n, k, sticks):
            if k == 0:
                return 0
            if k == n:
                return 1
            if sticks[n][k] is None:
                sticks[n][k] = place_sticks(n - 1, k - 1, sticks) + (n - 1) * place_sticks(n - 1, k, sticks)
            return sticks[n][k]
        
        sticks = [[None for _ in range(k + 1)] for _ in range(n + 1)]
        return place_sticks(n, k, sticks) % (10 ** 9 + 7)
        