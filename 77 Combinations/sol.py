"""
Approach: place an item, and then recurse with k - 1 items to place.
When k = 0, it means we have placed all the items, and so we can add a solution.

The combinations are created by the  `create_combinations` function, that takes 4 parameters:
- n, the maximum number to be used in the combinations
- starting: the starting number for the next combinations
- results: an array containing all the combinations
- current: the current combination that we are building.

At every step, place on item in the current combination, recurse and then remove the item, to allow the next iterations to work properly.

O(n! / ((n - k)!)) time, O(k * (n!) / ((n - k)!)) space
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def create_combinations(n, starting, k, results, current):
            if k == 0:
                results.append(list(current))
            else:
                for item in range(starting, n + 1):
                    current.append(item)
                    create_combinations(n, item + 1, k - 1, results, current)
                    current.pop(-1)
        
        results = []
        create_combinations(n, 1, k, results, [])
        return results
                