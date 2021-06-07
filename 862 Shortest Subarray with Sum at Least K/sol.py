"""
We have a trivial solution consisting in trying all the contiguous subarrays, and take the best one. O(N^2) time, O(1) space.
One observation: if k is in nums, answer is 1
Negative numbers are the problem. The following input is a good example of why a simple sliding window doesn't work
[-1, 1, 2, -1, 2]
3
because the subarray [1,2] is not seen, since its running sum in the window [0, 2] doesn't reach the target.
The prefix sum can help us
In addition to that, we use a deque, that will contain the possible values of the left pointer of the window. 
That is because we have negative number, and so the window can jump around and not be sequential
The key is keeping the deque increasing. In other words, the prefix sum of deque[0] >= prefix sum of deque[1].
This is helpful because if the current sum of the right pointer with the left of the queue is smaller than k, 
then all the other elements of the queue will also bring to a result smaller than k.
So we do three things:
- as the last operation of the main loop, we push the current index at the end of the queue. We will be sure that all the previous items will have a smaller prefix sum
- We keep removing from the top of the queue while the sum between the current pointer and the left of the queue is >= k.
- As soon as we break the previous condition, we remove all the items that are greater than the prefix sum in the current pointer

O(N) time and space
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque
        
        prefix_sum = [0]
        for item in nums:
            prefix_sum.append(prefix_sum[-1] + item)
        queue = deque()
        best_len = float('inf')
        for i in range(len(nums) + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                best_len = min(best_len, i - queue.popleft())
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(i)
        return best_len if best_len != float('inf') else -1