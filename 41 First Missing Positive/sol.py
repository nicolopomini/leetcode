"""
We use the array itself to keep track of what is missing.
The idea is that the first item will tell whether 1 is missing or not, the second item will tell is 2 is missing or not, and so on. Therefore, index i will tell if i + 1 is missing or not.

First thing: put all the non positive numbers out of range, e.g. setting them to 2 ** 31
Then, for all the items smaller or equal than the lenght of the array (the solution cannot be greater than the len of the array, we will have for sure some other missing value before), go to their index (e.g. if current item is 5, go to index 4) and negate the number (negate the abs, so that if it was already been negated it stays negative). 
Now we need to look for the first non negative item in the array: that will indicate the missing value! In case all the values are negative, it means that the input array was containing [1,... len(array)], and therefore the answer is len(array) + 1

O(N) time, O(1) space
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        out_of_range = 2 ** 31
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = out_of_range
        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                nums[abs(nums[i]) - 1] = -1 * abs(nums[abs(nums[i]) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1