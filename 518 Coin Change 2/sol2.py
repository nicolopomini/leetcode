"""
Simpler way:
For every coin in the coins list, try to build a change of all the amounts from 0 to the amount itself using that particular coin.
Store the results into an array
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for _ in range(amount + 1)]
        ways[0] = 1
        for coin in coins:
            for n in range(1, amount + 1):
                if n - coin >= 0:
                    ways[n] += ways[n - coin]
        return ways[-1]