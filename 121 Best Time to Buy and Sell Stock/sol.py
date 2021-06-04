"""
Since we have to buy one day and sell on a following day, we have to scan the input array left to right.
At every position, we can simulate to sell on that day, when we previously bought at a local minimum. 
So basically we keep track of the minumum price we faced before the current position, and we try to sell today.
Once we sold, we try to update the minimum to today

O(N) time, O(1) space
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last_min = float('inf')
        for item in prices:
            # try to sell today
            profit = max(profit, item - last_min)
            # update the minimum
            last_min = min(last_min, item)
        return profit