"""
We use three pointers:
- left indicating the next item scanned in the array
- right indicating the last item scanned in the array
- zero_pointer indicating the next position in which a 0 will be placed.
If we meet a 0 with the left pointer, we place it on the zero_pointer position and we increment the two pointers, 
If we face a 2, we put it at the end and we decrement the right pointer, 
otherwise we just increment the left pointer.
O(N) time, single pass, O(1) space
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        zero_pointer = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero_pointer] = nums[zero_pointer], nums[left]
                left += 1
                zero_pointer += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1