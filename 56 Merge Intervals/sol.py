"""
We can sort the intervals by starting time.
Then we push the first interval in the result array. Then for each other interval, consider the last interval in the result array, and if they can be merge, merge them.

O(n logn) time, O(n) space
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]
            if current[0] <= last[1]:
                result[-1] = [last[0], max(last[1], current[1])]
            else:
                result.append(current)
        return result