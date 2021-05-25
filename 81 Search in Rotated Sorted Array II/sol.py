"""
The array is divided into two subarrays, each of them is sorted.
We know that all the elements of the first are greater or equal than all the elements of the second.
So when searching, if the current middle value is greater than the first item of the array, two things can happen:
1. if the start is greater or equal than the target, and the target is smaller than the middle element, it means that the pivot is on our right hand side, and the target is on the left instead
2. Otherwise we search on the right
Symmetrically, if the current value is smaller that the first item of the array, two things can happen:
1. if the target is greater than the middle value, and the end item is greater or equal than the target, it means that we are on the right of the pivot, but also the target is on the right
2 Otherwise, search on the left
The problem is when the current value is equal to the first element of the array, because the target can be in both the sides. We can reduce the search space only by one position.

O(N) time in worst case, O(log N) on average, O(1) time
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return True
            if nums[middle] > nums[start]:
                if target < nums[middle] and nums[start] <= target:
                    end = middle - 1
                else: 
                    start = middle + 1
            elif nums[middle] < nums[start]:
                if target > nums[middle] and nums[end] >= target:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                start += 1
        return False