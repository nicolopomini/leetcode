"""
Similar to knapsack. If we have an amount == n, we can use one denomination, and solve for n - denomination

Base cases:
- amount = 0 => 0
- no coins => +inf
- amount < 0 => +inf
- otherwise: 1 + min {amount - c, for c in coins}.

Save partial results in a hash table, using memoization

O(amount) time and space
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change(amount, coins, cache):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in cache:
                return cache[amount]
            number_of_coins = float('inf')
            for c in coins:
                number_of_coins = min(number_of_coins, change(amount - c, coins, cache))
            cache[amount] = 1 + number_of_coins
            return cache[amount]
        
        number_of_changes = change(amount, coins, {})
        return -1 if number_of_changes == float('inf') else number_of_changes