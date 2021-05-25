"""
One possibility is to consider every pillar as the end of the rectangle, and then go back in the array to see how big such a rectangle can be.
O(N^2) time, O(1) space.

Otherwise, we can use a stack to help us in finding the largest rectangle we can create with the current rectangle that is on the right of the right pillar.
We keep a stack containing all the previous rectangles, in order from left (bottom of the stack) to right (top of the stack).
Suppose we are at position i, and there are k rectangles in the stack. What we can do is try to build a rectangle ending at i - 1, of height = the item at the top of the stack (popping it), and starting at the new top of the stack + 1.
Basically, in the stack we put indexes of pillars, and at every position we check what we can do with the pillar right before us.
In order to consider also the last pillar, we have to push a 0 in the input array.
We keep popping items from the stack until the new top of the stack is smaller than our current position in the input array, this is because using the popped item as height, we can also use its successors (that are smaller or equal than itself).
O(N) time and space, since every pillar is pushed and popped from the stack exactly once.

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        best = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                height_index = stack.pop(-1)
                start_index = -1 if not stack else stack[-1]
                best = max(best, heights[height_index] * (i - start_index - 1))
            stack.append(i)
        return best