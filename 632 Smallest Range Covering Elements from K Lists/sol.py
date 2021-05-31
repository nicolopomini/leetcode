"""
What if we start by considering all the first items of the lists, and we keep track of the minimum and the maximum. We save the range.
To make the range smaller, we have to change the smallest item, hoping to reduce the range.
So we remove the smallest item and we advance the pointer in that array, adding a new element, computing the new range and comparing them.
When we reach the last element of one of the array we can stop, since no other ranges can be smaller than the current.
We start from a range [-inf, inf], and we use two heaps to keep track of the min and the max. The items of the heaps are instances of ArrayItem, a custom class that contains the value of the item, and the index of the array it belongs to and the index inside the array.

O(N * log(k)) time, O(kN) space, where N is the length of the longest array, and k is the number of arrays
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def is_range_smaller(range1, range2):
            a, b = range1
            c, d = range2
            if b - a == d - c:
                return a < c
            return b - a < d - c
        
        import heapq
        
        min_heap = []
        max_heap = []
        best_range = [float('-inf'), float('inf')]
        for k in range(len(nums)):
            min_heap.append(ArrayItem(nums[k][0], k, 0))
            max_heap.append(-nums[k][0])
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)
        while True:
            current_range = [min_heap[0].value, -max_heap[0]]
            if is_range_smaller(current_range, best_range):
                best_range = current_range
            current_min = heapq.heappop(min_heap)
            if current_min.element_index + 1 == len(nums[current_min.array_index]):
                break
            new_element = nums[current_min.array_index][current_min.element_index + 1]
            heapq.heappush(min_heap, ArrayItem(new_element, current_min.array_index, current_min.element_index + 1))
            heapq.heappush(max_heap, -new_element)
        return best_range
            
        
        
        
class ArrayItem:
    def __init__(self, value, array_index, element_index):
        self.value = value
        self.array_index = array_index
        self.element_index = element_index
    
    def __lt__(self, o):
        return self.value < o.value