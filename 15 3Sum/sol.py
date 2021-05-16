"""
With the naive solution we could use a set to keep track of all the triplets (sorting them and saving as tuple).
We can do better: since the array is sorted, we can look for duplicates at the end of the results, so every time we try to add a new triplet, 
check the last one that was added.
In addition to that, skip the current first item of triplets in case it is equal to the previous first one.

O(N^2) time and space
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    candidate = [nums[i], nums[j], nums[k]]
                    if not results or results[-1] != candidate:
                        results.append(candidate)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return results