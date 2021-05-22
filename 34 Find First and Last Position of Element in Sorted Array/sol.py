"""
Two phases:
1. Search for the target in the array. If we don't find it, return [-1, -1]
2. Once found at index i, search the first appearance in array[: i] included, and the last into array[i: ].
First appearance: index i such that array[i] == target and (i == 0 or array[i - 1] < target)
Last appearance: index i such that array[i] == target and (i == len(array) - 1 or array[i + 1] > target).

O(log n) time, O(1) space
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_first_appearance(array, target, start, end):
            while start <= end:
                middle = (start + end) // 2
                if array[middle] == target:
                    if middle == 0 or array[middle - 1] < target:
                        return middle
                    else:
                        end = middle - 1
                else:
                    start = middle + 1
        
        def search_last_appearance(array, target, start, end):
            while start <= end:
                middle = (start + end) // 2
                if array[middle] == target:
                    if middle == len(array) - 1 or array[middle + 1] > target:
                        return middle
                    else:
                        start = middle + 1
                else:
                    end = middle - 1
        
        start = 0
        end = len(nums) - 1
        first_appearance = -1
        last_appearance = -1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                first_appearance = search_first_appearance(nums, target, start, middle)
                last_appearance = search_last_appearance(nums, target, middle, end)
                break 
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return [first_appearance, last_appearance]