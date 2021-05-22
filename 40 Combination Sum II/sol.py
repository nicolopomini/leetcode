"""
We need to sort the candidates. In order to avoid creating duplicated solutions, we need to skip some indexes:
- if we have already added the current candidate, we need to skip all the successors that have the same value, they will be added by the recursive calls, and therefore we don't have to add them now
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def build_combinations(candidates, target, current_sum, current_combination, current_index, results):
            if current_sum == target:
                results.append(list(current_combination))
                return
            if current_sum > target:
                return
            for i in range(current_index, len(candidates)):
                if i > current_index and candidates[i] == candidates[i - 1]:
                    continue
                current_combination.append(candidates[i])
                build_combinations(candidates, target, current_sum + candidates[i], current_combination, i + 1, results)
                current_combination.pop(-1)
        
        results = []
        candidates.sort()
        build_combinations(candidates, target, 0, [], 0, results)
        return results