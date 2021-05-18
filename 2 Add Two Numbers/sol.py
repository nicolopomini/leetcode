"""
Since they are in reversed order, we can just traverse the two lists in parallel, keeping track of the reminder in case the sum is over 9.
O(n + m) time and space
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = None
        result_tail = None
        reminder = 0
        while l1 and l2:
            local_sum = reminder + l1.val + l2.val
            node = ListNode(local_sum % 10)
            if not result_head:
                result_head = node
            else:
                result_tail.next = node
            result_tail = node
            reminder = int(local_sum / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            local_sum = reminder + l1.val
            node = ListNode(local_sum % 10)
            if not result_head:
                result_head = node
            else:
                result_tail.next = node
            result_tail = node
            reminder = int(local_sum / 10)
            l1 = l1.next
        while l2:
            local_sum = reminder + l2.val
            node = ListNode(local_sum % 10)
            if not result_head:
                result_head = node
            else:
                result_tail.next = node
            result_tail = node
            reminder = int(local_sum / 10)
            l2 = l2.next
        if reminder > 0:
            node = ListNode(reminder)
            if not result_head:
                result_head = node
            else:
                result_tail.next = node
        return result_head