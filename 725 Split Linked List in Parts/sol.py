"""
K can be smaller, equal or greater than the length of the list.
Approach 1: count how long is the list, compute how many nodes must go in each part, and then scan again the list to produce the parts.
O(N) time and space (because if size of each part is 1, the output size is O(N))
How many items in each part? The final parts are going to have len(list) // k items, while the first ones will have one element more.
Which of them? The first size % k parts.
Instead of creating a new list, we split the existing one, and we return an array of pointers, containing the heads of the parts
"""
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        def get_size(head):
            current = head
            size = 0
            while current and current.next:
                current = current.next.next
                size += 2
            if current:
                size += 1
            return size
        
        list_size = get_size(root)
        part_size = list_size // k
        longer_parts = list_size % k
        current = root
        result = []
        for _ in range(longer_parts):
            result.append(current)
            for _ in range(part_size):
                current = current.next
            if current:
                local = current
                current = current.next
                local.next = None
        for _ in range(k - longer_parts):
            if part_size == 0:
                result.append(None)
            else:
                result.append(current)
                for _ in range(part_size - 1):
                    current = current.next
                if current:
                    local = current
                    current = current.next
                    local.next = None
        return result
                