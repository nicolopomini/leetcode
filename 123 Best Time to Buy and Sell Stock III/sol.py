"""
At most 2 transactions.
We have to sell before buying again, and we can sell on a following day after we bought.
Step 1: simulate the best we can do on every day with one transaction
Step 2: use the best we did on the day before the current with 1 transaction, and try to use the second one.
To do so, keep track of the best profit we have achieved with 1 transaction before today, and then try to sell today and buy yesterday

O(N) time and space
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_with_one_transaction = [0]
        min_so_far = prices[0]
        for i in range(1, len(prices)):
            best_with_one_transaction.append(max(best_with_one_transaction[i - 1], prices[i] - min_so_far))
            min_so_far = min(min_so_far, prices[i])
        best_so_far = float('-inf')
        profit = 0
        for i in range(1, len(prices)):
            best_so_far = max(best_so_far, best_with_one_transaction[i - 1] - prices[i - 1])
            profit = max(profit, best_so_far + prices[i])
        return profit
        