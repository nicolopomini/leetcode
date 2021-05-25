"""
Pretty straightforward.
It would also be possible to do the following: once we find the third duplicate in a row, we check if other duplicates follow, and then we shift all the remaining items backwards
O(N^2) time, O(1) space
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        prev = nums[0]
        prev_count = 1
        while i < len(nums):
            if nums[i] == prev:
                if prev_count == 2:
                    nums.pop(i)
                else:
                    prev_count += 1
                    i += 1
            else:
                prev = nums[i]
                prev_count = 1
                i += 1
        return len(nums)