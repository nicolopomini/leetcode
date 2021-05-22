"""
Just apply the recursive formula. We need to compute all the sequence from 1 until n, storing the previous one.
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say_string(string):
            result = []
            last_char = string[0]
            count = 1
            for i in range(1, len(string)):
                if string[i] == last_char:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(last_char)
                    last_char = string[i]
                    count = 1
            result.append(str(count))
            result.append(last_char)
            return "".join(result)
        
        prev_sequence = "1"
        for i in range(2, n + 1):
            prev_sequence = count_and_say_string(prev_sequence)
        return prev_sequence