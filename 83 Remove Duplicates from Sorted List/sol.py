"""
Scan the list keeping track of the last visited item. Update the next pointer only when the item we are visiting has a different value than the previous.
O(N) time, O(1) space
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        current = head
        while current:
            if not prev:
                prev = current
            elif prev.val != current.val:
                prev.next = current
                prev = current
            current = current.next
        prev.next = None
        return head