"""
Use a hashmap to count how many times an item appears into the array.
Then pick one element as first item of the permutations, and recurse removing 1 from the counter of such an item. After that, replace its counting.
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def count_elements(array):
            counter = {}
            for item in array:
                if item not in counter:
                    counter[item] = 0
                counter[item] += 1
            return counter
        
        def compute_permutations(counters, current, results):
            if not counters:
                results.append(current)
            else:
                # need to store all the keys because then the dict is mutated
                current_keys = list(counters.keys())
                for item in current_keys:
                    # choose the item as the next element to be added in the perm.
                    counters[item] -= 1
                    # if no more items left, remove the key from the dict
                    if counters[item] == 0:
                        counters.pop(item)
                    compute_permutations(counters, current + [item], results)
                    # put back to the original status for the next recursions
                    if item not in counters:
                        counters[item] = 0
                    counters[item] += 1
        
        counters = count_elements(nums)
        results = []
        compute_permutations(counters, [], results)
        return results