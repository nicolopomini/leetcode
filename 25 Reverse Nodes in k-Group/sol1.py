"""
Easier solution, using a stack to contain the portion of the list that will be reversed next.
We use a counter i to keep track of how many nodes we pushed into the stack, and when i reaches k - 1, it's time to reverse.
Reversing:
- store the next node (`curr`), that will be pointed by the new tail of the reversed portion
- The first one that is popped must be pointed by the current predecessor, all the others must point to the node right behind them in the stack.
- Finally, we update the tail of the reversed portion of the stack, pointing to `curr`
- Reset stack and counter.

O(N) time, since every node is pushed and popeed from the stack at most once, O(k) space
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev = head
        is_head = True
        i = 0
        curr = head
        stack = []
        while curr is not None and i < k:
            stack.append(curr)
            if i == k - 1:
                curr = curr.next
                for j in range(i, 0, -1):
                    node = stack[j]
                    if j == i: # first one
                        if is_head:
                            head = node
                            is_head = False
                        else:
                            prev.next = node
                    node.next = stack[j - 1]
                node = stack[0]
                prev = node
                node.next = curr
                i = 0
                stack = []
            else:
                i += 1
                curr = curr.next
        return head