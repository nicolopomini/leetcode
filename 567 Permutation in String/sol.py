"""
One permutation of s1 must be in s2
1. I need to count the characters in s1, since all its permutations will be made by the same characters
"abc" => a: 1, b: 1, c: 1
I can also count in parallel the counter of the character appearing in the first window inside s2.
If all the counters match, we can return true
Then we move inside s2, checking the other windows.
We firstly remove the leftmost character, by decreasing its counter in the window array.
If before the decreasing, that character was matching exactly the same char in s1, we have to decrement the number of matching letters
On the other hand, if after decreasing it we get a counter that is the same of s1, we increase the number of matching letters
Symmetrically, we add the rightmost char in the window

O(1) space, O(s2) time
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_counters = [0 for _ in range(26)]
        window = [0 for _ in range(26)]
        matching_letters = 0
        # count the characters of s1 and the first window of s2
        for i in range(len(s1)):
            s1_counters[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        # check if the first window is a permutation
        for i in range(26):
            if s1_counters[i] == window[i]:
                matching_letters += 1
        if matching_letters == 26:
            return True
        for i in range(len(s1), len(s2)):
            char_to_add = s2[i]
            char_to_remove = s2[i - len(s1)]
            if window[ord(char_to_remove) - ord('a')] == s1_counters[ord(char_to_remove) - ord('a')]:
                matching_letters -= 1
            window[ord(char_to_remove) - ord('a')] -= 1
            if window[ord(char_to_remove) - ord('a')] == s1_counters[ord(char_to_remove) - ord('a')]:
                matching_letters += 1
            window[ord(char_to_add) - ord('a')] += 1
            if window[ord(char_to_add) - ord('a')] == s1_counters[ord(char_to_add) - ord('a')]:
                matching_letters += 1
            elif window[ord(char_to_add) - ord('a')] == s1_counters[ord(char_to_add) - ord('a')] + 1:
                matching_letters -= 1
            if matching_letters == 26:
                return True
        return matching_letters == 26
            