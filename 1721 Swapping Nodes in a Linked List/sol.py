"""
We can just swap the values, the problem is identifying the two nodes.
We can just count, starting from 1 and going ahead in the list.
Once we find the first node, we save it into a pointer, and we start counting using two pointers:
- the first one is at the head of the list
- the second one at the node we found
We make them go ahead one step at a time simultaneously, until the second reaches the end; the other one will point to the second node
We then swap the values and return the head
O(N) time, O(1) space
"""
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        current = head
        count = 1
        while count < k:
            count += 1
            current = current.next
        first_node = current
        second_node = head
        while current.next:
            current = current.next
            second_node = second_node.next
        first_node.val, second_node.val = second_node.val, first_node.val
        return head
        