"""
We have to find the two vertical lines that define the rectangle with the largest area.
We can start from the largest rectangle, compute its area and store it.
Then we can reduce the window removing the smallest side and going on the next line on that direction,
and see if the new area is larger than the best one.
Keep doing so until the two lines are the same one.

O(N) time, O(1) space
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        largest_area = min(height[start], height[end]) * (end - start)
        while start < end:
            if height[start] < height[end]:
                start += 1
            else: 
                end -= 1
            largest_area = max(largest_area, min(height[start], height[end]) * (end - start))
        return largest_area