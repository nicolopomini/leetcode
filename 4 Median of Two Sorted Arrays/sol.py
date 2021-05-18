"""
We have to figure with item(s) would be in the middle of the sorted merging of the two arrays.
The final array would be partitioned into two parts: the one below the half, and the other above the half. We know the size of the two partitions [ that is (len(nums1) + len(nums2)) / 2].
The goal is partitioning the two arrays, such that the union of the two left partitions would create the left partition of the big array, and the union of the two right partitions would create the right partition of the big array.

Supposing that one partition ends at index i in the first array, and the other partition ends at index j in the other array, the two partitions are good if:
 nums1[i] < nums2[j + 1] and nums2[j] < nums1[i + 1].
 
 How to find the partitions? take the shortest array and compute its middle value; that's the end of its partition. The end of the other partition is: (len(nums1) + len(nums2)) / 2 - len of the first partition.
 Check if the partitions are good.
 If not, apply binary search on the shortest array: if nums1[i] >= nums2[j], we have to find the middle on the left of i, otherwise on the right of i
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = end = len(nums1)
        n = len(nums2)
        start = 0
        idx_middle = (m+n+1) // 2 # Center index of final merged array
        
        while start <= end:
            partition1 = (start + end) // 2 
            partition2 = idx_middle - partition1
            
            maxleft1 = nums1[partition1-1] if partition1 != 0 else -float('inf')
            minright1 = nums1[partition1] if partition1 != m else float('inf')
            maxleft2 = nums2[partition2-1] if partition2 != 0  else -float('inf')
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
                if (m+n) % 2 == 0:
                    min_of_right = min(minright1, minright2)
                    return (max_of_left + min_of_right)/2
                else:
                    return max_of_left