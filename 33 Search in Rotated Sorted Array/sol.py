"""
The array increases for k steps, then jump down to the minimum, and then keep increasing until the end.
1. Find the index where the lowest number is, using binary search
2. Once we know the shifting position, apply binary search to find the value.


2. A sorted array shifted by k positions (es by k=5)
We do a normal binary search, middle = (((start + end) / 2) + k) % n
if is the target, boom.
If greater than the target, update middle (without shift and mod) to end - 1
otherwise middle = start + 1

O(log n) time, O(1) space

1. we want to find i such that array[i] < array[i - 1].
Base case: check if the lowest item is at position 0, if array[0] < array[-1]
if we are at pos k, and array[k] < array[k - 1], we found the index
if array[k] > array[k - 1] and array[k] > array[-1], search on the right
search on the left

O(log n) time, O(1) space

Overall: O(log n) time, O(1) space
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_shift_index(array):
            if array[0] < array[-1]:
                return 0
            start = 1
            end = len(array) - 1
            while start <= end:
                middle = int((start + end) / 2)
                if array[middle] < array[middle - 1]:
                    return middle
                elif array[middle] > array[middle - 1] and array[middle] > array[-1]:
                    start = middle + 1
                else:
                    end = middle - 1

        def shifted_search(array, target, shift_index):
            n = len(array)
            start = 0
            end = n - 1
            while start <= end:
                middle = int((start + end) / 2)
                shifted_middle = (middle + shift_index) % n
                if array[shifted_middle] == target:
                    return shifted_middle
                elif array[shifted_middle] > target:
                    end = middle - 1
                else:
                    start = middle + 1
            return -1
        
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        shift_index = search_shift_index(nums)
        return shifted_search(nums, target, shift_index)