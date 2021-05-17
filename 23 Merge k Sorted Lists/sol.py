"""
We can use a min-heap containing, for each of the k lists, their current minimum item.
The heap must contain the nodes of the lists.

At the beginning, add into the heap the first item of every list. Then get the minimum, put it into the result list, and add to the heap the following node of the list where the node we just used comes from.
Keep going until there are nodes to be used.

The heap will have a size of at most k, so inserting and getting items from it is taking O(log k) time, and the heap takes O(k) memory.
We are going to operate on all the items in the list, we can call it n. 

Overall: O(k) space since we are using the already existing nodes, O(n logk) time
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = MinHeap()
        result_head = None
        result_tail = None
        for i in range(len(lists)):
            if lists[i]:
                heap.insert(HeapItem(lists[i]))
        while not heap.is_empty():
            item = heap.remove()
            if not result_head:
                result_head = item.node
            else:
                result_tail.next = item.node
            result_tail = item.node
            if item.node.next:
                heap.insert(HeapItem(item.node.next))
        return result_head
        

class HeapItem:
    """
    Used a class just to implement the __lt__ method, that is handy in the min-heap.
    If using a built-in heap, is handy too
    """
    def __init__(self, node):
        self.node = node
        
    def __lt__(self, o):
        return self.node.val < o.node.val

    
class MinHeap:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def _sift_up(self, index):
        parent_index = int((index - 1) / 2)
        if self.items[index] < self.items[parent_index]:
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
            self._sift_up(parent_index)
    
    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        minimum = index
        if left_child_index < len(self.items) and self.items[left_child_index] < self.items[minimum]:
            minimum = left_child_index
        if right_child_index < len(self.items) and self.items[right_child_index] < self.items[minimum]:
            minimum = right_child_index
        if index != minimum:
            self.items[index], self.items[minimum] = self.items[minimum], self.items[index]
            self._sift_down(minimum)
            
    
    def insert(self, item):
        self.items.append(item)
        self._sift_up(len(self.items) - 1)
    
    def remove(self):
        item = self.items[0]
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        self.items.pop(-1)
        if len(self.items) > 0:
            self._sift_down(0)
        return item
        