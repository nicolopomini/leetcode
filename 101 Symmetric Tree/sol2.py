"""
Recursive approach: two trees are symmetrical if the two roots are the same, and the left children of one is symmetrical to the right children of the other, and viceversa.
O(N) time, O(h) space
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def are_symmetrical(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return are_symmetrical(root1.left, root2.right) and are_symmetrical(root1.right, root2.left)
        
        return are_symmetrical(root.left, root.right)