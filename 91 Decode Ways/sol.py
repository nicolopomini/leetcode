"""
For convenience, we store the strings from 1 to 26 into a set, for an easy and fast lookup.
We store into an array ways[i] the number of ways to decode the string[i:]
If i == len(string) - 1, the number of ways is 1 if string[-1] is in the set, 0 otherwise, or if i >= len(string), the result is 1
Otherwise, ways[i] = ways[i + 1] if string[i] in set, + ways[i + 2] if string[i] + string[i + 1] in the set.

Actually, we can only store the next two item of ways, to make the algorithm work in constant space.
O(N) time, O(1) space
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        codes = set([str(i) for i in range(1, 27)])
        ways_plus_one = 1
        ways_plus_two = 1
        ways = 1 if s[-1] in codes else 0
        for i in range(len(s) - 2, -1, -1):
            ways_plus_two = ways_plus_one
            ways_plus_one = ways
            ways = 0
            if s[i] in codes:
                ways += ways_plus_one
            if s[i] + s[i + 1] in codes:
                ways += ways_plus_two
        return ways