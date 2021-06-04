"""
We can make any number of transactions.
The rule is that I have to buy on day x and sell on day > x, and only when I sell I can buy again.
What is the max profit I can achieve on every day?
Day 0 is 0, since I can only buy
Day 1 is profit of day 0 + (buy at dy 0 and sell today) or don't do anything
Day N is don't do anything (= day N - 1) or day N - 1 + (buy at day N - 1 and sell today), this is because in day N - 1 I already computed the best I can do on that day
O(N) time, O(1) space
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(1, len(prices)):
            best_profit = max(best_profit, best_profit + prices[i] - prices[i - 1])
        return best_profit
        