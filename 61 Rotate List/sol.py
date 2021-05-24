"""
4 things to know:
- current head
- current tail => where node.next is None
compute k mod len(list)
- new head => reachable in len(list) - k steps from the current head. If k == n, head and tail unchanged
- the new tail => reachable in len(list) - k - 1 from the current head, or len(list) - k steps from the current tail.
Overall, we traverse the list twice, so O(N) time and O(1) space
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length = 1
        current_tail = head
        while current_tail.next is not None:
            length += 1
            current_tail = current_tail.next
        k = k % length
        if k == 0:
            return head
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        current_tail.next = head
        return new_head