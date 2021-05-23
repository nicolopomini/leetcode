"""
Base solution: try all the subarray, keeping track of their sum while creating them and updating the best sum found. O(N^2) time, O(1) space

Can we do better? We can compute the maximum subarray starting at every position of the array. The maximum one is the answer.
max[i] = {
    array[i] if i == len(array) - 1
    max(array[i], array[i] + max[i + 1]) otherwise
}
O(N) time and space
But since we only look into the successor value (to determine max[i] we only look at max[i + 1]) we can use constant space!
O(N) time, O(1) space
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[-1]
        max_in_next_pos = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            local_max = max(nums[i], nums[i] + max_in_next_pos)
            max_subarray = max(max_subarray, local_max)
            max_in_next_pos = local_max
        return max_subarray