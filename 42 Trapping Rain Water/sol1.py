"""
One solution: using extra memory.
Scan the array left to right, and keep track of the highest pillar. The area full of water in each position is the the difference between the highest pillar and the current pillar. Store these values into an array.
Then scan the array right to left, doing computing the same difference: if the difference is smaller than the one in the array, overright it.
Finally, return the sum of the array.
O(N) time and space
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        water_area = [0]
        highest_pillar = height[0]
        for i in range(1, len(height)):
            highest_pillar = max(highest_pillar, height[i])
            water_area.append(highest_pillar - height[i])
        highest_pillar = height[-1]
        for i in range(len(height) - 1, -1, -1):
            highest_pillar = max(highest_pillar, height[i])
            area = highest_pillar - height[i]
            water_area[i] = min(water_area[i], area)
        return sum(water_area)