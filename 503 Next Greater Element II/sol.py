"""
Similar to next greater element I, we keep a stack containing the indexes of the items that haven't been assigned a successor yet.
The stack will contain a decreasing sequence, so the first item that is greater than the top of the stack is going to be the successor
of the top of the stack.
We have to traverse the array twice, in order to allow the latest element to get their successor too
O(N) time and space
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def find_successor(nums, stack, result):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    predecessor_index = stack.pop()
                    result[predecessor_index] = nums[i]
                stack.append(i)
        
        result = [-1 for _ in nums]
        stack = []
        find_successor(nums, stack, result)
        find_successor(nums, stack, result)
        return result
        