"""
1 -> 0, 1
2 -> 00, 01, 11, 10
3 -> 000, 001, 011, 010, 110, 111, 101, 100
read left to right, prepend a 0 to every element
read right to left, prepend a 1 to every element
use the last sequence as new array.
The base case is when n = 1.
O(2^N) time and space
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = ['0', '1']
        for _ in range(1, n):
            new_codes = []
            for i in codes:
                new_codes.append('0' + i)
            for i in reversed(codes):
                new_codes.append('1' + i)
            codes = new_codes
        return [int(n, 2) for n in codes]
        