"""
We have to figure with item(s) would be in the middle of the sorted merging of the two arrays.
The final array would be partitioned into two parts: the one below the half, and the other above the half. We know the size of the two partitions [ that is (len(nums1) + len(nums2)) / 2].
The goal is partitioning the two arrays, such that the union of the two left partitions would create the left partition of the big array, and the union of the two right partitions would create the right partition of the big array.

We apply binary search on the shortest array to search the two partitions inside of it. As a consequence, once fixed the partition in the shortest array, we also have the partition in the longest one.
We are good if the max of the left partition of array 1 is smaller than the min of the right partition of array 2, and if the max of the left partition of array 2 is smaller than the min of the right partition of array 1.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = end = len(nums1)
        n = len(nums2)
        start = 0
        idx_middle = (m + n + 1) // 2 # Center index of final merged array. We use +1, because in case of odd array the result will fall into the left partition
        
        while start <= end:
            partition1 = (start + end) // 2 
            partition2 = idx_middle - partition1
            
            maxleft1 = nums1[partition1 - 1] if partition1 != 0 else float('-inf')
            minright1 = nums1[partition1] if partition1 != m else float('inf')
            maxleft2 = nums2[partition2 - 1] if partition2 != 0  else float('-inf')
            minright2 = nums2[partition2] if partition2 != n else float('inf')
            
            if maxleft1 > minright2:
                # move nums1 end to before partition
                end = partition1 - 1
            elif maxleft2 > minright1:
                # move nums1 start to after partition
                start = partition1 + 1
            else:
                # Found the right partition!
                # if odd, ans is max(maxleft1, maxleft2)
                # if even, ans is avg of max(maxleft1, maxleft2) and min(minright1, minright2)
                max_of_left = max(maxleft1, maxleft2)
                if (m + n) % 2 == 0:
                    min_of_right = min(minright1, minright2)
                    return (max_of_left + min_of_right) / 2
                else:
                    return max_of_left