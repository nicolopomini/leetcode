"""
Trivial solution: try all the subarrays. O(N^2) time, O(1) space.
To make things more optimal, we can use a sliding window.
We keep two pointers, left and right, and we increase the right one until the current sum in the window is >= target.
Then, we try to reduce the size of the window, stopping when we reach the right pointer, or if the current sum becomes < target.
O(N) time, O(1) space
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current_sum = 0
        best_len = float('inf')
        while right < len(nums):
            current_sum += nums[right]
            while left <= right and current_sum >= target:
                if current_sum >= target:
                    best_len = min(best_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1
        return best_len if best_len != float('inf') else 0