"""
If k=1, it means that we can only rotate the input string. That is, at every step we put the first letter to the end, and the second letter becomes the new first one. In this case we have to find the rotation with the smallest lexicographical ordering.
If k > 1, we can produce any permutation of the string. That is because with k = 2 we can swap any couple of characters (sending the second to the back, than the first one, and then shifting), so the answer is the string ordered alphabetically
O(N^2) time, O(N) space
"""
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return "".join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))