"""
We keep a hashtable to count the number of characters inside the current window, and an integer counter representing how many types of characters on the t string are covered by the window. The latter is used in case t contains some duplicated letters. The counters will be positive for the characters in t, and negative for all the others.
e.g. s = "ADOBECODEBANC", t = "ABC". At the beginning A,B,C will count 1, all the others to 0.
We start scanning s, and at every character we see we decrement its counter. If the counter goes to 0, it means that it is contained in t and that we satisfied that letter, so we can increment the integer counter. When counter reaches the number of unique characters in t, we found a window. We can save it and start reducing it.
When reducing it, we remove one letter at a time incrementing its counting in the hashtable. If a counter was at 0, it means that such a letter is in t, and therefore our current window is missing that character. Therefore we increase the integer counter by one, and we start again by increasing the window.
Continue like this until the right side of the window reaches the end of the string.
We keep track of the legth of the best window, to know the case in which the initial window has not been modified, and in such a case it means that there's no window

O(N) time and space
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build hashmap
        counters = {c: 0 for c in s}
        for c in t:
            if c not in counters:
                # in this case the window cannot exist, since s does not contain all the letters of t
                return ""
            counters[c] += 1   
        satisfied_chars = 0
        unique_chars_in_t = len(set(t))
        best_window_left = 0
        best_window_right = len(s) - 1
        left = 0
        right = 0
        size = float('inf')
        while right < len(s):
            # add the char pointed by right
            char = s[right]
            counters[char] -= 1
            if counters[char] == 0:
                satisfied_chars += 1
            if satisfied_chars == unique_chars_in_t:
                # we have a window!
                if best_window_right - best_window_left >= right - left:
                    best_window_right = right
                    best_window_left = left
                    size = right - left + 1
            # reduce the window size
            while left <= right and satisfied_chars == unique_chars_in_t:
                if best_window_right - best_window_left >= right - left:
                    best_window_right = right
                    best_window_left = left
                    size = right - left + 1
                left_char = s[left]
                if counters[left_char] == 0:
                    satisfied_chars -= 1
                counters[left_char] += 1
                left += 1
            right += 1
        return s[best_window_left: best_window_right + 1] if size != float('inf') else ""