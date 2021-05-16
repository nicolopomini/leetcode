"""
Reverse a linked list in groups of k nodes.
Before doing so, we traverse ahead of k nodes from the current point, to know wehre the next reverse will start. 
The function `get_kth_ahead` returns the k-th node ahead of the current position (can be null) and a boolean indicating whether there are at list k nodes after the current position,
and therefore we must reverse. In this way, when we call `reverse`, we are sure we have at least k nodes, and the reverse function does not need to handle edge cases.
The reverse function returns the new head and the new tail of the portion of the list that has been reversed.
We need to keep track of the tail of the last portion that was reversed in the previous iteration, to connect the two pointers together and not to lose part of the list.
Another edge case is the first reversion, where we have to update the main head of the list. That's why we use the variable `is_head`.
Finally, we need to update the last reversed tail to point to the remaining part of the list (either null if k is multiple of the lenght of the list, or the first not-reversed node)

O(N) time, O(1) space
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def get_kth_ahead(current, k):
            # returns a node and a boolean indicating whether there are k nodes after current
            for i in range(k):
                if i < k - 1 and not current.next:
                    return None, False
                current = current.next
            return current, True
        
        def reverse(current, k):
            prev = None
            succ = None
            tail = current
            for _ in range(k):
                succ = current.next
                current.next = prev
                prev = current
                current = succ
            return prev, tail
        
        is_head = True
        new_head = None
        current = head
        last_reversed_tail = None
        must_reverse = True
        while must_reverse and current:
            k_th_ahead, must_reverse = get_kth_ahead(current, k)
            if must_reverse:
                reversed_head, reversed_tail = reverse(current, k)
                if is_head:
                    is_head = False
                    new_head = reversed_head

                if last_reversed_tail:
                    last_reversed_tail.next = reversed_head
                last_reversed_tail = reversed_tail
                current = k_th_ahead
        if last_reversed_tail:
            last_reversed_tail.next = current
        return new_head