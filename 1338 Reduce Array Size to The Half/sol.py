"""
Greedy approach:
1. We count the frequency with which every item appears in the array.
2. We sort the appearances by decreasing order
3. We keep removing items until the size of the set is below the half of the original size.

O(N logN) time, O(N) space
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequences = {}
        for item in arr:
            if item not in frequences:
                frequences[item] = 0
            frequences[item] += 1
        current_size = len(arr)
        sorted_frequences = sorted(frequences.values(), reverse=True)
        count = 0
        while current_size > len(arr) // 2:
            current_size -= sorted_frequences[count]
            count += 1
        return count