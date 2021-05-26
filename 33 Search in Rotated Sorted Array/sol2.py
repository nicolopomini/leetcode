"""
The array is divided in two parts:
- the first one that increases until a pivot index
- the second one that is stricty lower than the first one, and increases until the end
Every item of the first part is greater than every item of the second one.
We can use these feature to create a binary search algorithm.
If the middle element is equal to the target, we are done, otherwise:
- if the middle element is lower than the first element of the array, it means that we are on the second part of the array: in this case, if target is greater than middle and lower than the start of the array, search on the right, otherwise on the left
- if the middle element is greater or equal than the first element of the array, we search on the left if target >= start and target < middle, otherwise on the right

O(log n) time, O(1) space
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < nums[start]:
                if target > nums[middle] and target < nums[start]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if target >= nums[start] and target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
        return -1