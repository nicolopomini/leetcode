"""
Let total be an array containing the prices for every stair
Cost of the last one is its value
Cost of the penultimate is its value
Otherwise: we have to pay our current cost, and then jump of the next or on the second next stair, choosing the one with the minimum cost
total[i] = cost[i] + min(total[i + 1], total[i + 2])
Finally, we pick the cheapest from total[0] and total[1]
We can do that in constant space, keeping track only of the next two stairs, and every time update the values
O(N) time, O(1) space
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next_cost = cost[-2]
        next_next_cost = cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            local_cost = cost[i] + min(next_cost, next_next_cost)
            next_next_cost = next_cost
            next_cost = local_cost
        return min(next_cost, next_next_cost)