"""
amount = 5, coins = [1,2,5]
How many ways can we create 5 using coin 5? 1
How many ways can we create 5 using coin 2? Using one of them or using 2 of them
How many ways can we create 5 using coin 1? Using either 1, 2, 3, 4 or 5 of them.

To change N using k types of coin, we can try to use 0, 1, 2, ... int(amount / coin) number of that coins, and then recurse, updating the amount based on how many coins we used before, and using the following coins only.

Params: amount, current index
Base case:
- index is the last: check if amount is multiple of the coin, in case it is return 1, otherwise no way of making a change 
General case:
- try to use an amount of the current coin, update the amount and go to the next coin

Use a hashtable to save subproblems results.
O(amount * coins) time and space
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def ways_of_change(amount, coins, index, cache):
            if index == len(coins) - 1:
                if amount % coins[-1] == 0:
                    return 1
                return 0
            if (amount, index) in cache:
                return cache[(amount, index)]
            coin = coins[index]
            max_usage = int(amount / coin)
            ways_to_change = 0
            for i in range(max_usage + 1):  # at least try to use 0 coins of this type
                used_amount = coin * i
                ways_to_change += ways_of_change(amount - used_amount, coins, index + 1, cache)
            cache[(amount, index)] = ways_to_change
            return ways_to_change
        
        return ways_of_change(amount, coins, 0, {})
