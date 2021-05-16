"""
General approach that can be extended to n-sum.
Sort the array and use 4 pointers.
To avoid duplicates:
- if the first pointer is equal to its predecessor, skip it
- if the second pointer is not right after the first pointer, and it's equal to its predecessor, skip it.
- when adding to the results, check whether the last added quadruplet is equal to the one we are about to add.

O(N^3) time, O(N^2) space
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        results = []
        for index_1 in range(len(nums) - 3):
            if index_1 > 0 and nums[index_1] == nums[index_1 - 1]:
                continue
            for index_2 in range(index_1 + 1, len(nums) - 2):
                if index_2 > index_1 + 1 and nums[index_2] == nums[index_2 - 1]:
                    continue
                index_3 = index_2 + 1
                index_4 = len(nums) - 1
                while index_3 < index_4:
                    value = nums[index_1] + nums[index_2] + nums[index_3] + nums[index_4]
                    if value == target:
                        candidate = [nums[index_1], nums[index_2], nums[index_3], nums[index_4]]
                        if not results or results[-1] != candidate:
                            results.append(candidate)
                        index_3 += 1
                        index_4 -= 1
                    elif value < target:
                        index_3 += 1
                    else:
                        index_4 -= 1
        return results