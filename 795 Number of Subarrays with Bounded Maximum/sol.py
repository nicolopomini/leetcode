"""
Find the number of contiguous subarray whose maximum element is left <= element <= right.
At every position we can start a new array, we can continue a previous array, or we have to stop in case the number is too high.
We can start a new array in case the current element is between bounds
We can continue another array if there is an array including the previous element and if the current element <= right: in this case the current item can become the new maximum
We cannot continue or start any array if current element > right.

How to detect how many open arrays we have?
[2,1,3,4,5,2,1] min = 2, max = 4
[2], [2, 1], [2,1,3], [1,3], [3], [2,1,3,4], [1,3,4], [3,4], [4], [2], [2, 1]

Let subs[i] the number of subarrays starting with nums[i]
subs[n - 1] = 1 if left <= array[n - 1] <= right, else 0
subs[i] = 0 if nums[i] > right
          subs[i + 1] if nums[i] < left
          otherwise, if left <= nums[i] <= right, we can start a number of subarrays that is equal to the distance between the i and the next item > right.
The answer is the sum of subs[i].

[2,1,3,4,5,2,1] min = 2, max = 4
[4,2,2,1,0,2,0]

Since subs[i] relies only on subs[i + 1], we can do that in constant space
O(N) time, O(1) space

"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        subarray_count = 1 if left <= nums[-1] <= right else 0
        last_greater = len(nums) if nums[-1] <= right else len(nums) - 1
        subs = subarray_count
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > right:
                subs = 0
                last_greater = i
            elif nums[i] < left:
                subarray_count += subs
            else:
                subs = last_greater - i
                subarray_count += subs
        return subarray_count
        