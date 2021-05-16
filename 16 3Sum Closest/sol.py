"""
Basically identical to three sum, use three pointers and scan all the triplets, saving the one that is the closest to the target.

O(N^2) time, O(1) space
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for s in range(len(nums) - 2):
            m = s + 1
            e = len(nums) - 1
            while m < e:
                value = nums[s] + nums[m] + nums[e]
                if abs(target - value) < abs(diff):
                    diff = target - value
                elif value > target:
                    e -= 1
                else:
                    m += 1
        return target - diff