"""
Some examples:
    1
2.      3
      4
must return [1, 3, 4]
Basically we need the rightmost node of every level.

Second approach: do a DFS preferring the right side of the tree. We keep track of the deepest level visited, and if the current node is the new deepest level, we add it to the result. Then we go right and left.
O(N) time, O(h) space
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def visit(node, current_depth, max_depth, results):
            # visit the tree rooted in node, knowing the previous max_depth reached.
            # the visit priviledges the right hand side of the tree, and the first time we go deeper than max_depth, we add the node to the results
            if not node:
                return max_depth
            if current_depth > max_depth:
                results.append(node.val)
                max_depth += 1
            max_depth = visit(node.right, current_depth + 1, max_depth, results)
            max_depth = visit(node.left, current_depth + 1, max_depth, results)
            return max_depth
        
        results = []
        visit(root, 0, -1, results)
        return results
            