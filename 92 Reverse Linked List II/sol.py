"""
We do it in one pass. We have to traverse the list until we reach the left counter, then we start reversing, keeping track of the last node before the reversing started.
The first node in the reversing portion will be the last one after the reversal, and so it will be connected with the first node of the portion after the reversed one.
O(N) time, O(1) space
"""
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        current = head
        prev = None
        while count < left:
            prev = current
            current = current.next
            count += 1
        last_before_reversing = prev
        # reversing
        new_last_node = current
        following = current.next
        prev = None
        while count <= right:
            current.next = prev
            prev = current
            current = following
            following = current.next if current else None
            count += 1
        # prev points to the new first node in the reversed portion
        if last_before_reversing:
            last_before_reversing.next = prev
        else:
            head = prev
        new_last_node.next = current
        return head
            
        