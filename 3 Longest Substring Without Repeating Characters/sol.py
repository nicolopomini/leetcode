"""
Use a sliding window to identify the start and the end of the current substring we are considering. 
Use a set to store the chars currently in the window, and try to expand it as much as possible (as long as we don't insert an already present char)
In case we are trying to do so, keep decreasing the window left to right, as long as we can insert the current char.
Keep going until we reach the end of the string with the right hand side of the window

O(n) time and space
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        best_left = 0
        best_right = 0
        current_chars = set()
        while right < len(s):
            # the char we want to add is already in the current window, let's decrease it
            while s[right] in current_chars:
                current_chars.remove(s[left])
                left += 1
            current_chars.add(s[right])
            right += 1
            if right - left > best_right - best_left:
                best_right = right
                best_left = left
        return best_right - best_left