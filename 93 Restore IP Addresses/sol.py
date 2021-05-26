"""
We try to put three dots in the middle of the string.
We can add a dot if the previous part of the string is an integer between 0 and 255, and it does not have leading zeros if not the number 0 itself.
We store all the partial ip inside an array, for performace reasons.
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid_part(string):
            number = int(string)
            return number < 256 and ((number == 0 and len(string) == 1) or string[0] != '0')
        
        def create_addresses(string, current, result, dots, index):
            if dots == 0:
                if is_valid_part(string[index:]):
                    current.append(string[index:])
                    result.append(".".join(current))
                    current.pop(-1)
            else:
                for i in range(index + 1, len(string)):
                    if is_valid_part(string[index: i]):
                        current.append(string[index: i])
                        create_addresses(string, current, result, dots - 1, i)
                        current.pop(-1)
            
        result = []
        create_addresses(s, [], result, 3, 0)
        return result