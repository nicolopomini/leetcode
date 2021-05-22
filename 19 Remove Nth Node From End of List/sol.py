"""
The easiest approach is traversing the list, counting the number of nodes in the list; then traversing again stopping at the right node and removing it.

We can start from the head counted as 1, and go ahead with a pointer of k positions. After that, we leave such a pointer where it is, and we start a new pointer at the beginning, moving these two pointers ahead together, until the right one reaches the end (i.e. it becomes null): the other will be on the node to be removed. So just track its predecessor and remove the node.
To remove it, we have the corner case in which the node can be the head (if predecessor is null)

O(N) time, O(1) space
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        right_pointer = head
        left_pointer = head
        prev = None
        for _ in range(n):
            right_pointer = right_pointer.next
        while right_pointer:
            prev = left_pointer
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        if not prev:
            # we are removing the head
            head = head.next
        else:
            prev.next = left_pointer.next
        return head