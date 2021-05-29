"""
We have a minimum profit to reach, max n people to use, and k crimes we can make to reach the profit.
If profit to reach <= 0, the current combination forms a solution
If we run out of people before reaching the profix, the current combination is not valid.
If we run out of crimes before reaching the profix, the current combination is not valid.

Let crimes[profit][people] the number of crimes giving profit = profit and requiring a number of people = people. All the combinations giving more that minProfit profit will be collapsed into profit = minProfit.
The base case is given by achieving profit = 0 using 0 people, and there is 1 way to do it: doing nothing. crimes[0][0] = 1.
For each crimes, we consider all the combinations of people G and profit P, and we add that crime, obtaining a profit = min(P + profit[i], minProfit) and a group of G + group[i].
Since we update all the table at every step, we need to clone before starting, and then override the original one.
O(n * minProfit * number of crimes) time
O(n * minProfit) space
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        crimes = [[0 for _ in range(n + 1)] for _ in range(minProfit + 1)]
        crimes[0][0] = 1
        for i in range(len(group)):
            crime_group = group[i]
            crime_profit = profit[i]
            new_crimes = [row[:] for row in crimes]
            for g in range(n + 1 - crime_group):    # at most n people, so we subtract the crime group
                current_group = g + crime_group
                for p in range(minProfit + 1):
                    current_profit = min(minProfit, p + crime_profit)
                    new_crimes[current_profit][current_group] += crimes[p][g]
            crimes = new_crimes
        return sum(crimes[minProfit]) % (10 ** 9 + 7)