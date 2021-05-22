"""
Using two pointers, one for the left and one for the right. The issue with this problem is risking to compute an area that is too larg. With this approach we include at every step the smallest side, either left or right, computing the maximum met on every side and adding the difference. In this way the tallest pillar will never be added to soon, and we will not have problems with computing an area that is too large.
O(N) time, O(1) space
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        area = 0
        while left <= right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                area += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                area += max_right - height[right]
                right -= 1
        return area