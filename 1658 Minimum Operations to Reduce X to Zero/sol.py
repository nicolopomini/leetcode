"""
At every step, we have to pick one side, reduce the array and x.
All the numbers in the array are positive, so once we subtract more than x we cannot go back anymore.
Optimal substructure, because to solve the problem for x and an array of n items, we have to use the best solution for x - item and an array of n - 1 elements.
MinOperations(i, j, x) returns the minimum number of operations to reduce x to zero using the array from i to j inclusive.
MinOperations(i, j, x):
+inf if x < 0
0 if x == 0
+inf if x > 0 and j < i
otherwise:
min(MinOperations(i + 1, j, x - array[i]), MinOperations(i, j - 1, x - array[j])) + 1
O(N^2 * X) time and space

Can we use a sliding window?
- if a side brings me to 0, choose that side
- if a side brings me below 0, choose the other side
- If there is an answer, this means that exists a subarray of sum totalSum - x, somewhere in the middle
- we want this subarray to be as long as possible, because the remaining part of the original array are the operations we have to take to minimize the number, and they have to be as low as possible

How to identify the longest subarray with that sum? We can use a sliding window.
O(N) time, O(1) space

"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        right = 0
        window_sum = 0
        longest_window = float('-inf')
        while right < len(nums):
            window_sum += nums[right]
            if window_sum == target:
                # right and left included
                longest_window = max(longest_window, right - left + 1)
            while window_sum >= target and left <= right:
                window_sum -= nums[left]
                left += 1
                if window_sum == target:
                    # right and left included
                    longest_window = max(longest_window, right - left + 1)
            right += 1
        return -1 if longest_window == float('-inf') else len(nums) - longest_window
        