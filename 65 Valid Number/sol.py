"""
Simply apply the definition: decimal or integer (+ optionally) an E + integer
Check for e:
- if not e, return is_decimal or is_integer
- otherwise return (is_decimal or is_integer until e) AND is_integer after E.

O(N) time, O(1) space
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(s, start, end):
            digits = [str(i) for i in range(10)]
            signs = ['+', '-']
            has_digits = False
            for i in range(start, end + 1):
                if s[i] in signs and i > start:
                    return False
                if s[i] not in digits and s[i] not in signs:
                    return False
                if s[i] in digits:
                    has_digits = True
            return has_digits
        
        def is_decimal(s, start, end):
            digits = [str(i) for i in range(10)]
            signs = ['+', '-']
            first_digit = None
            last_digit = None
            dot_index = None
            for i in range(start, end + 1):
                if s[i] in signs and i > start:
                    return False
                if s[i] == '.':
                    if dot_index is not None:
                        return False
                    dot_index = i
                if s[i] in digits:
                    last_digit = i
                    if first_digit is None:
                        first_digit = i
                if s[i] not in digits and s[i] not in signs and s[i] != '.':
                    return False
            if first_digit is None:
                return False
            if dot_index is not None:
                return last_digit < dot_index or dot_index < first_digit or first_digit < dot_index < last_digit
            return True
        
        e_index = s.find('e')
        if e_index == -1:
            e_index = s.find('E')
        if e_index == -1:
            return is_integer(s, 0, len(s) - 1) or is_decimal(s, 0, len(s) - 1)
        if e_index == 0 or e_index == len(s) - 1:
            return False
        return (is_integer(s, 0, e_index - 1) or is_decimal(s, 0, e_index - 1)) and is_integer(s, e_index + 1, len(s) - 1)
        