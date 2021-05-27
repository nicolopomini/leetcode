"""
BFS, visiting the tree level by level.
O(N) time and space
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from queue import Queue
        q = Queue()
        result = []
        level = []
        current_level = None
        q.put((root, 0))
        while not q.empty():
            node, lev = q.get()
            if current_level is not None and current_level != lev:
                result.append(level)
                level = []
            current_level = lev
            level.append(node.val)
            if node.left:
                q.put((node.left, lev + 1))
            if node.right:
                q.put((node.right, lev + 1))
        result.append(level)
        return [l for l in reversed(result)]
        