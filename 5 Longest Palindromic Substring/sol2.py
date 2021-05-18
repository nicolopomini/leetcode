"""
Use DP tp discover the length of the longest palindrome.
We use a table `is_palindrome[i][j]` that contains a boolean indicating whether the string from i to j (both inclusive) is palindrome.

Base cases: 
- strings of len 1 are palindrome
- strings of len 2 are palindrome if the two characters are the same

General case: 
- for every string of length at least 3, until lenght N:
    - if the first and the last characters are the same, and the string from the second to the penultimate is palindrome, then the string we are considering is palindrome too.
Every time we update the table we keep track of the current longest palindrome we faced.

O(N^2) time and space
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome = [[False for _ in s] for _ in s]
        longest_start = 0
        longest_end = 0
        for i in range(len(s)):
            is_palindrome[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                longest_start = i
                longest_end = i + 1
        for length in range(3, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if s[start] == s[end] and is_palindrome[start + 1][end - 1]:
                    is_palindrome[start][end] = True
                    if end - start > longest_end - longest_start:
                        longest_start = start
                        longest_end = end
        return s[longest_start: longest_end + 1]