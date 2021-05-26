"""
Simple recursive solution: 2 trees are the same if:
roots are the same, subtrees are the same.
O(N) time, O(h) space
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        is_root_equal = p.val == q.val
        are_left_equal = self.isSameTree(p.left, q.left)
        are_right_equal = self.isSameTree(p.right, q.right)
        return is_root_equal and are_left_equal and are_right_equal
        