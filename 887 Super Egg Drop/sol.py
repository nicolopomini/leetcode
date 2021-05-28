"""
We have to find f such that breaks(f) is false, and breaks(f + 1) is True. Of course we don't know how breaks(x) works.
We can approach the problem in the following ways: given M moves and K eggs, how many floor do I have to check?
floors[M][K] = floors[M - 1][K - 1] (if egg breaks) + floors[M - 1][K] (if egg doesn't break) + 1 (the current check on the current floor).
As soon as the number of floors we check with k eggs is greater of equal than N, we have the answer in the current number of moves we are on
O(NK) time and space
"""
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        floors = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for move in range(1, n + 1):
            for eggs in range(1, k + 1):
                floors[move][eggs] = 1 + floors[move - 1][eggs - 1] + floors[move - 1][eggs]
            if floors[move][k] >= n:
                return move