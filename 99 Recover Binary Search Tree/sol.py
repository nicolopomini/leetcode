"""
The nodes can be neighbours (parent and child) or distant (node and a non-direct descendant).
The inorder visit of a BST gives us the items sorted. We can use that to detect anomalies and fix them.
Two cases:
- the nodes are not adjacent in the visit order
    1
3
  2
here the visit order is [3,2,1] and the two nodes to be swapped are 1 and 3
So we need to find two nodes that are not adjacent. A better example is with a larger array, such as [1,5,3,4,2,6]. We notice the first node when the predecessor of our current node is greater than us, so we need to keep track of the predecessor. The second node is the next one in which we face the anomaly, but in this case the node to store is the current one, and not the previous

- the nodes are adjacent in the visit order:
    3
1       4
      2
here the visit order is [1,3,2,4] and the nodes to be swapped are 2 and 3.
In this case we keep a pointer with the previous node, and if the previous is bigger than the current, we swap the values.

We do a in order visit of the tree, keeping track of these nodes.
The recursive function that does the visit takes as parameters the previous node in the visit, and two other nodes indicating the first anomaly. It may update them and returning as well.
In case we have two anomalies, the visit itself takes care of swapping the right nodes, otherwise if only one anomaly is detected, the wrapper function does the swap

O(N) time, O(h) space
"""
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def visit(node, prev = None, first_anomaly_node = None, prev_first_anomaly_node = None):
            if not node:
                return prev, first_anomaly_node, prev_first_anomaly_node
            prev, first_anomaly_node, prev_first_anomaly_node = visit(node.left, prev, first_anomaly_node, prev_first_anomaly_node)
            if prev and prev.val > node.val:
                # we have an anomaly
                # we can be the first one (and maybe the only one)
                if not first_anomaly_node:
                    first_anomaly_node = node
                    prev_first_anomaly_node = prev
                else:
                    # another anomaly was detected previously, we just swap the node with its predecessor here
                    prev_first_anomaly_node.val, node.val = node.val, prev_first_anomaly_node.val
                    first_anomaly_node = None
                    prev_first_anomaly_node = None
            prev, first_anomaly_node, prev_first_anomaly_node = visit(node.right, node, first_anomaly_node, prev_first_anomaly_node)
            return prev, first_anomaly_node, prev_first_anomaly_node
        
        _, first_anomaly_node, prev_first_anomaly_node = visit(root)
        if first_anomaly_node:
            first_anomaly_node.val, prev_first_anomaly_node.val = prev_first_anomaly_node.val, first_anomaly_node.val
        