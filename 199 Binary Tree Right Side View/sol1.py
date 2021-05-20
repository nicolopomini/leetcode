"""
Some examples:
    1
2.      3
      4
must return [1, 3, 4]
Basically we need the rightmost node of every level.
First approach: visit the tree level by level, and add in the result the rightmost node (i.e. the last of the level). 
O(N) time, O(D) space, where D is the diameter of the tree
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque
        
        if not root:
            return []
        queue = deque()
        result = []
        queue.append((root, 0))
        last_seen_level = 0
        last_seen_node = None
        while len(queue) > 0:
            node, level = queue.popleft()
            if level > last_seen_level:
                result.append(last_seen_node.val)
            last_seen_node = node
            last_seen_level = level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        result.append(last_seen_node.val)
        return result
            
        