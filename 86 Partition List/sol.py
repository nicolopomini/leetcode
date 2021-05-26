"""
Keep two separate linked lists: one containig all the items smaller than x, and the other with all the remaining ones.
At the end, merge the two lists.
O(N) time, O(1) space
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_than = LinkedList()
        greater_equal_than = LinkedList()
        while head:
            if head.val < x:
                smaller_than.add(head)
            else:
                greater_equal_than.add(head)
            head = head.next
        if smaller_than.is_empty():
            return greater_equal_than.head
        smaller_than.extend(greater_equal_than)
        smaller_than.tail.next = None
        return smaller_than.head
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def is_empty(self):
        return self.head is None
    
    def extend(self, linked_list):
        if linked_list.is_empty():
            return
        self.tail.next = linked_list.head
        self.tail = linked_list.tail
