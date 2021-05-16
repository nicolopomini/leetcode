"""
Use a sliding window:
- start with the largest window possible, and compute the area of water that can fit.
- Reduce the window on the side where the wall is shorter

O(n) time, O(1) space
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        best = (end - start) * min(height[start], height[end])
        while start < end:
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            best = max(best, (end - start) * min(height[start], height[end]))
        return best