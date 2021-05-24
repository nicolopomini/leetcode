"""
need to find i such that:
- intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]
there might not be a predecessor or a successor, in case newInterval is before the first one or after the last one, a corner case

need to check whether newInterval must be merged with intervals[i], intervals[i + 1] or both of them

- newInterval totally before intervals[i] => append intervals[i]
- newInterval overlapped with intervals[i] => consider [min(starts), max(ends)] and using it as predecessor
- predecessor comes before intervals[i] => append predecessor, append intervals[i]

O(N) time and space
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        predecessor = newInterval
        for item in intervals:
            if not predecessor:
                result.append(item)
            elif item[1] < predecessor[0]:
                result.append(item)
            elif item[0] > predecessor[1]:
                result.append(predecessor)
                result.append(item)
                predecessor = None
            else:
                # end of item is >= the beginnning of new interval
                # end new interval <= beginning of item
                predecessor[0] = min(predecessor[0], item[0])
                predecessor[1] = max(predecessor[1], item[1])
        if predecessor:
            result.append(predecessor)
        return result
        
        