"""
0 -> 0
1 -> 1
2 -> 2
3 -> pick the root and distirbute nodes on the leaves.
start with the lowest node as root: left empty, right n - 1
second node, left with 1, right with n - 2
so on until last node, with left n - 1 and right n - n

3:
1: 0 2 => 2
2: 1 1 => 1 * 1
3: 2 0 => 2

4:
1: 0 3 => 5
2: 1 2 => 2
3: 2 1 => 2
4: 3 0 => 5

O(n) space, O(n^2) time
"""
class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1, 2]
        for i in range(2, n):
            # doing n = i + 1
            number_of_trees = 0
            left = 0
            right = i
            for root in range(1, i + 2):
                res = 1
                if left > 0:
                    res *= trees[left - 1]
                if right > 0:
                    res *= trees[right - 1]
                number_of_trees += res
                left += 1
                right -= 1
            trees.append(number_of_trees)
        return trees[n - 1]