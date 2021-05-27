"""
DFS, keeping an array of arrays, level by level, and returning it reversed.

O(N) time and space
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def visit(node, result, level):
            if not node:
                return
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
            visit(node.left, result, level + 1)
            visit(node.right, result, level + 1)
        
        result = []
        visit(root, result, 0)
        return list(reversed(result))