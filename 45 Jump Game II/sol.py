"""
We keep track the number of steps we can make before being forced to do another jump.
Then, every time we try to increase the maximum point we can get using the current position.
In case we run out of steps, we are forced to take a jump, and we update the number of steps we can make with the difference between the maximum position we can reach and the current position we are on.

O(N) time, O(1) space
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        steps = nums[0]
        jumps = 1
        reached = nums[0]
        for i in range(1, len(nums) - 1):
            reached = max(reached, i + nums[i])
            steps -= 1
            if steps == 0:
                steps = reached - i
                jumps += 1
        return jumps