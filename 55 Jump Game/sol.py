"""
We can keep track of the maximum index we can reach, doing any number of steps. If we are able to reach the end of the array, we return True. If from a given position i, we are not able to do any step further, we return False
O(N) time, O(1) space
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        for i in range(len(nums)):
            max_distance = max(max_distance, i + nums[i])
            if max_distance >= len(nums) or i == len(nums) - 1:
                return True
            if max_distance == i:
                return False    # we are stuck