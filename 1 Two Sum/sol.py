"""
Store the numbers into a hashtable, containing a list of indexes (in case of duplicates)
Scan again the array, and for each element check if there is its complementary.
In case there is, check that is not equal to the current number, or in case it is check that we have at least two elements with the same value
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = []
            numbers[nums[i]].append(i)
        for n in nums:
            candidate = target - n
            if candidate in numbers:
                if candidate != n:
                    return [
                        numbers[n][0],
                        numbers[candidate][0]
                    ]
                elif len(numbers[n]) > 1:
                    return [
                        numbers[n][0],
                        numbers[n][1]
                    ]