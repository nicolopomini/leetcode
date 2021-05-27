"""
BFS approach, level by level. Keep an array on the current level, and verify whether it is symmetrical.

O(N) time, O(d) space
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from queue import Queue
        q = Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            node1 = q.get()
            node2 = q.get()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            q.put(node1.left)
            q.put(node2.right)
            q.put(node1.right)
            q.put(node2.left)
        return True