"""
This problem has an optimal substructure: once we covered some columns, we are left with another portion of the board. The optimal solution of the remaining part is part of the optimal solution of the entire part.
Solving left to right:
Base case: n = 0, there is 1 way of tiling the board, living it empty
n = 1: there is 1 way of tiling the board, by placing a 2x1 domino tile vertically.
General case: we can do one of the following:
- place a 2x1 tile vertically, and use the solution with n - 1 columns
- place 2 2x1 tiles horizontally, one above the other, and use the solution with n - 2 columns
- use the L shape tiles: place an L, and then we have n - 2 columns completely empty, and one column with the upper row empty. The solution is upper(n - 1)
- use the reversed L shape, leaving the next column empty in the lower row, and all the other rows empty. This is lower(n - 1)
Overall, the solution for a board of n is equal to sol(n - 1) + sol(n - 2) + upper(n - 1) + lower(n - 1).
How to solve upper(n)? Placing an horizontal 2x1 tile, and having lower(n - 1), or placing a reversed L and solving sol(n - 2)
Similarly, lower(n) is equal to sol(n - 2) + upper(n - 1).

Base cases:
n = 0, we have sol(0) = 1, lower() = 0, upper(0) = 0
n = 1: sol(1) = 1, lower() = 0, upper(0) = 0

Expanding the equation:
Upper(n) = sol(n - 2) + lower(n - 1)
Lower(n) = sol(n - 2) + upper(n - 1)
Sol(n) = sol(n - 1) + sol(n - 2) + upper(n - 1) + lower(n - 1)

Putting together:
Sol(n) = sol(n - 1) + sol(n - 2) + [sol(n - 3) + lower(n - 2) + sol(n - 3) + upper(n - 2)]
that can be regrupped in
Sol(n) = sol(n - 1) + sol(n - 3) + [sol(n - 2) + sol(n - 3) + lower(n - 2) + upper(n - 2)], and the term in square brackets is exactly Sol(n - 1), therefore
Sol(n) = 2 * sol(n - 1) + sol(n - 3)
"""
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        n_minus_three = 1
        n_minus_two = 1
        n_minus_one = 2
        for i in range(3, n + 1):
            current = 2 * n_minus_one + n_minus_three
            n_minus_three = n_minus_two
            n_minus_two = n_minus_one
            n_minus_one = current
        return n_minus_one % (10 ** 9 + 7)