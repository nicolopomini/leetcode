"""
We need to swap a node with its successor, and then repeat again, only if the node has a successor.
Given the current node, we check if it has a successor: in case it has, we swap them and we move to the third node.
The corner case is the first swap, when we have to change the head of the list
O(N) time, O(1) space
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            if current.next:
                # there is a successor, swap them!
                second = current.next
                successor = current.next.next
                second.next = current
                current.next = successor
                # update the predecessor
                if not prev:
                    head = second
                else:
                    prev.next = second
                # finally, make the loop continue correctly
                prev = current
                current = successor
            else:
                current = current.next
        return head