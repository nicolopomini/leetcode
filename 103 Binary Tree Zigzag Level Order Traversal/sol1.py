"""
BFS visit, keeping an array of each level
O(n) time, O(n) space
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        from queue import Queue
        q = Queue()
        q.put((root, 0))
        result = []
        level = []
        going_left = True
        prev_h = None
        while not q.empty():
            node, h = q.get()
            if prev_h is not None and prev_h != h:
                if going_left:
                    result.append(level)
                else:
                    result.append([x for x in reversed(level)])
                level = []
                going_left = not going_left
            prev_h = h
            level.append(node.val)
            if node.left:
                q.put((node.left, h + 1))
            if node.right:
                q.put((node.right, h + 1))
        
        if going_left:
            result.append(level)
        else:
            result.append([x for x in reversed(level)])
        return result