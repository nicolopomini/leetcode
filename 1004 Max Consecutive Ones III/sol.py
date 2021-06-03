"""
Indentify all the portions of the input array that are made of ones.
Creating a list [[start, end]] where each item contains two integers, respectively the start and end index (inclusive) of a 1 sequence.
But it can be tricky to merge them.
We can try with a sliding window:
- we start the window at the first position, and we increase it towards right: if the item we add is already a 1, just increase the counter of the items involved,
otherwise decrease k by one. When k = 0 and we face a 0, we cannot increase the window anymore. We have to move the left pointer, until it reaches the right one, or we face an item that is 0, which is removed from the window, and therefore k is increased.
O(N) time, O(1) space
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        longest_window = 0
        while right < len(nums):
            if nums[right] == 1:
                longest_window = max(longest_window, right - left + 1)
                right += 1
            elif k > 0:
                k -= 1
                longest_window = max(longest_window, right - left + 1)
                right += 1
            else:
                while left <= right and k == 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
        return longest_window