"""
Since there are duplicates, we need to count items to avoid creating duplicates.
Then we generate all the combinations for a single number, based on the number of times such a number appears in the input array.
Finally, we use a similar technique to the one used for generating the powerset, appending to every existing result a combination
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def get_counters(nums):
            counters = {}
            for n in nums:
                if n not in counters:
                    counters[n] = 0
                counters[n] += 1
            return counters
        
        def create_combinations(number, count):
            combinations = []
            for i in range(count):
                combinations.append([number for _ in range(i + 1)])
            return combinations
        
        counters = get_counters(nums)
        result = [[]]
        for number in counters:
            combinations = create_combinations(number, counters[number])
            updated_result = []
            for res in result:
                for comb in combinations:
                    updated_result.append(res + comb)
            result.extend(updated_result)
        return result
        