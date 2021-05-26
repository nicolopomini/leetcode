"""
Iterative solution
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack[-1]
            del stack[-1]
            result.append(curr.val)
            curr = curr.right
        return result