"""
We expand candidate palindrome strings from their centers.
A palindrome of odd length has one char in center, while a palindrome of even length has two.
In total, there are 2n - 1 centers to test, and each test takes O(n) time.
Therefore, O(n^2) time, O(n) space (the returned string)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return start + 1, end - 1
        
        longest_palindrome_start = 0
        longest_palindrome_end = 0
        for i in range(len(s) - 1):
            start, end = expand_from_center(s, i, i)
            if end - start > longest_palindrome_end - longest_palindrome_start:
                longest_palindrome_start = start
                longest_palindrome_end = end
            if s[i] == s[i + 1]:
                start, end = expand_from_center(s, i, i + 1)
                if end - start > longest_palindrome_end - longest_palindrome_start:
                    longest_palindrome_start = start
                    longest_palindrome_end = end
        start, end = expand_from_center(s, len(s) - 1, len(s) - 1)
        if end - start > longest_palindrome_end - longest_palindrome_start:
            longest_palindrome_start = start
            longest_palindrome_end = end
        return s[longest_palindrome_start: longest_palindrome_end + 1]