"""
We need to keep track of the last seen value, the first node containing such a value and its predecessor, and the last one containing the value. 
When we see a node that has the same value of the last value, we just update the last container.
Instead, in case the node we are visiting has a different value, we have to see if we have to remove the previous nodes.
- If the first and the last node containing the previous value, nothing to remove, just set the first and the last node to the current one and go on.
- Otherwise, we have to make the predecessor of the first node containing the previous value with the current node. The edge case is when the head is the first node containing a duplicate value.

O(N) time, O(1) space
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        first_node_with_value = head
        last_node_with_value = head
        prev_of_first_node = None
        current = head.next
        prev = head
        while current:
            if current.val == last_node_with_value.val:
                last_node_with_value = current
            elif first_node_with_value == last_node_with_value:
                # only one node with the previous value, nothing to do if not just update the first and last pointer
                prev_of_first_node = prev
                first_node_with_value = current
                last_node_with_value = current
            else:
                if prev_of_first_node:
                    prev_of_first_node.next = current
                else:
                    head = current
                first_node_with_value = current
                last_node_with_value = current
            prev = current
            current = current.next
        if first_node_with_value != last_node_with_value:
            # the last nodes are duplicated, remove them
            if prev_of_first_node:
                prev_of_first_node.next = None
            else:
                head = None
        return head
                
                        
        