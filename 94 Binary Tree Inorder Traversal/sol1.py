"""
Recursive solution
O(N) time, O(h) space
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node: TreeNode, result: list):
            if node is not None:
                traverse(node.left, result)
                result.append(node.val)
                traverse(node.right, result)
        
        result = []
        traverse(root, result)
        return result