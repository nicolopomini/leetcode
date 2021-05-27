"""
Recursive solution with DFS.
Keep an array or arrays (the final result), where the array at position i is the level i.
If such a level does not exist already in the result, create it.
Then visit the current node, the tree on the left and the one on the right.

O(N) time, O(n) space
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def visit(node, result, level):
            if not node:
                return
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            visit(node.left, result, level + 1)
            visit(node.right, result, level + 1)
        
        result = []
        visit(root, result, 0)
        return result