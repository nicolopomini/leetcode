"""
If one of the two is empty, intersection is empty
Similarly, when all the intervals of one array have been processed, there are no more possible intersections
We start by considering the first intervals in the two lists:
- the one ending first
- the other one (they may end at the same time actually)
If they are overlapped (start of first <= end second, or start second <= end first) we create the intersection (max of starts, min of ends), and we advance the pointer of the list of the one ending first
otherwise, we advance the pointer of the list of the one ending first.

O(N) time and space
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            first_start, first_end = firstList[p1]
            second_start, second_end = secondList[p2]
            do_intersect = (first_start <= second_end and first_end >= second_start) or (second_start <= first_end and second_end >= first_start)
            if do_intersect:
                intersection = [max(first_start, second_start), min(first_end, second_end)]
                result.append(intersection)
            if first_end < second_end:
                p1 += 1
            else:
                p2 += 1
        return result
        