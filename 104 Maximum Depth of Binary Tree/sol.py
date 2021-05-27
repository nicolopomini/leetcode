"""
Simple recursive visit, keeping track of the maximum level that every subtree reaches.
If we passed a leaf, the max depth was the one of the leaf.
O(N) time, O(h) space
"""
class Solution:
    def maxDepth(self, root: TreeNode, level: int = 1) -> int:
        if not root:
            return level - 1
        return max(self.maxDepth(root.left, level + 1), self.maxDepth(root.right, level + 1))