"""
For every subarray, I need to compute the sum of its elements and the minimum element contained.
The sum can be computed using the prefix sum, and then given i and j obtain the sum of the subarray in constant time.
Brute force solution: try all the subarrays: O(N^2) time, O(1) space.

At the end of the day, this problem is an evolution of the largest rectangle in histogram.
The only difference is that we have to take the sum of the elements, instead of the width of the rectangle.
The approach is going to be the same, except that we need to keep also the prefix sum of the array to compute the sum of the elements of a rectangle.
At each position we try a rectangle ending at i - 1, starting at (top of the stack + 1) of height the top of the stack.
O(N) time and space
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for item in nums:
            prefix_sum.append(item + prefix_sum[-1])
        largest_product = 0
        stack = []
        nums.append(0)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                min_element = nums[stack.pop(-1)]
                index_before_start = -1 if not stack else stack[-1]
                # prefix sum is shifted by one, so to get the sum of the array[index_before_start + 1: i - 1 inclusive]
                # i need to do prefix_sum[final_pos + 1] - prefix_sum[end_pos] 
                subarray_sum = prefix_sum[i] - prefix_sum[index_before_start + 1]
                largest_product = max(largest_product, min_element * subarray_sum)
            stack.append(i)
        return largest_product % (10 ** 9 + 7)