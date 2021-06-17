"""
Letters outside square brackets can just be reported as they are on the output.
As soon as we face a digit, we have to parse it, to know its value, and then we will face an open braket: 
from there on, keep reading and storing the input until a closing bracket is found. Then add the part of input 
between the brakets k times in the output.
Since the brackets can contain other brackets, we can use the recursive stack to keep track of a braket not already parsed completely
O(N) time and space
"""
class Solution:
    def decodeString(self, s: str) -> str:
        def is_digit(char):
            return '0' <= char <= '9'
        
        def parse_string(string, index):
            # index is the starting index
            # returns the parsed string, and the last index of the string (e.g. the ] bracket)
            result = []
            number = 0
            while index < len(string) and string[index] != ']':
                char = string[index]
                if is_digit(char):
                    number = (number * 10) + int(char)
                elif char == '[':
                    string_among_brackets, index = parse_string(string, index + 1)
                    for _ in range(number):
                        result.append(string_among_brackets)
                    number = 0
                else:
                    result.append(char)
                index += 1
            return "".join(result), index
        
        parsed, _ = parse_string(s, 0)
        return parsed
                