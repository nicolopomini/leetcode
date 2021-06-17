"""
I need to map the elements of the first array to their index
Then, for every element in the second array, I need to find their next greater element.
I can use a stack to push the indexes of the items of the second array for which I still haven't found a next greater element.
As soon as I visit an item, and there are items on the stack, I can pop from the stack the indexes pointing to items smaller
than the current element. The current element will be their successor, so then I update the successor of the item in the first array
O(N + M) time and space
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index_map = {nums1[i]: i for i in range(len(nums1))}
        result = [-1 for _ in nums1]
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                if nums2[index] in nums1_index_map:
                    result[nums1_index_map[nums2[index]]] = nums2[i]
            stack.append(i)
        return result