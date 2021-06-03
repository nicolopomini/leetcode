"""
Local inversions: if array[i] > array[i + 1]
Global inversions: given j > i, array[i] > array[j]

Of course this is solvable in O(N^2) time, checking all the global inversions and comparing them to the local ones
Ideas:
- compare the array with the original permutation, from 0 to n - 1

Of course a local inversion is also a global inversion
1,0 is both the things
2,1,0 => 2 local and 3 global
1,0,3,2 => 3 local and 2 global
Compare every number with the value on the same position in the original permutation. If it is just swapped with its successor or predecessor it is fine and we can continue, otherwise the number of inversion cannot be equal.
This is because all global inversions must be local inversions, and therefore the position of number with value i cannot be farther than i +- 2

O(N) time, O(1) space
"""
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if abs(i - nums[i]) > 1:
                return False
        return True