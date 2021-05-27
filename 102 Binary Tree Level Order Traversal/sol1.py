"""
BFS visit with a queue, storing the pair <node, level>
O(n) time, O(n) space, where l is the largest level of the tree
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        from queue import Queue
        q = Queue()
        q.put((root, 0))
        result = []
        level = []
        prev_h = None
        while not q.empty():
            node, h = q.get()
            if prev_h is not None and prev_h != h:
                result.append(level)
                level = []
            prev_h = h
            level.append(node.val)
            if node.left:
                q.put((node.left, h + 1))
            if node.right:
                q.put((node.right, h + 1))
        result.append(level)
        return result
        
        