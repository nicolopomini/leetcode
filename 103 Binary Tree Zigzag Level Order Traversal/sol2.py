"""
Same recursive solution of the previous problem, with the difference that we need to reverse the arrays in odd positions.

O(N) time and space
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = list(reversed(result[i]))
        return result