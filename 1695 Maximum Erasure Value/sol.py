"""
The goal is to find the subarray made by unique elements with the largest sum, and return its sum.
Naive option: try all subarrays, checking when building it if it is made by unique values and computing on the fly its sum. O(N^2) time, O(1) space.

As alternative, we can use a sliding window to track the current piece of array we are considering, and a set to store the values currently in the window.
We increase the sliding window towards left, until we reach the end of the array or when the item we add is already in the window.
In the second case, we have to reduce the windown increasing the left pointer, until we remove an item that is equal to the last character we added.
The largest sum of any window we faced is the answer.
O(N) time and space
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_sum = 0
        current_sum = 0
        items = set()
        while right < len(nums):
            last_added = nums[right]
            if last_added not in items:
                items.add(last_added)
                current_sum += last_added
                if current_sum > max_sum:
                    max_sum = current_sum
                right += 1
            else:
                while left <= right:
                    last_removed = nums[left]
                    items.remove(last_removed)
                    left += 1
                    current_sum -= last_removed
                    if last_removed == last_added:
                        break
        return max_sum
                