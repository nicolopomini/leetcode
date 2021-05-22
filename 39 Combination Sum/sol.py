"""
Recursive approach: we have to build all the combinations, and therefore we have to try all the combinations.
A combination is good if its sum is equal to the target. So while building one combination we have to keep track of the current sum. In addition to that, we need to keep track of the current index in the array of candidate we are. We always stay where we are or we go forward, but never back, to avoid creating duplicated results.

How to build a combination? Using a function build_combinations(candidates, target, current_sum, current_combination, current_index, results)
if the current sum is equal to the target, we have a combination, that will be added in the results
If the current sum is too big, just return
Otherwise: for every index from the current_index until the end of the array, we add the index to the solution and we recurse. In this way we can reuse the same candidate as many times as we want, and we also explore all the others.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def build_combinations(candidates, target, current_sum, current_combination, current_index, results):
            if current_sum == target:
                results.append(list(current_combination))
                return
            if current_sum > target:
                return
            for i in range(current_index, len(candidates)):
                current_combination.append(candidates[i])
                build_combinations(candidates, target, current_sum + candidates[i], current_combination, i, results)
                current_combination.pop(-1)
        
        results = []
        build_combinations(candidates, target, 0, [], 0, results)
        return results