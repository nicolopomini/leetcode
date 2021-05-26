"""
We use a range of values to verify the validity of the binary tree.
In addition to verify the structure of the tree, we have to check if the value lays in the range, and then update the range.
O(n) time, O(h) space
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root, min_value, max_value):
            if not root:
                return True
            cond = min_value < root.val < max_value
            if root.left:
                cond = cond and root.val > root.left.val
            if root.right:
                cond = cond and root.val < root.right.val
            return cond and isValid(root.left, min_value, root.val) and isValid(root.right, root.val, max_value)
        
        return isValid(root, float('-inf'), float('inf'))
        