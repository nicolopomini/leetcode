"""
We proceed backwards, starting from the target and removing the last stamp.
stamp = "abca", target = "aabcaca". To be a possible solution, we must have a substring in target that is equal to stamp; if not, return empty array.
We remove the last stamp from the target, obtaining "a????ca", and storing the initial index (1), then all the '?' will become a wildcard that matches any character.
When to stop? Either when all the string is made by '?', or if no substring match the stamp.

Space: O(target), since we transform the target string into an array for performance reason. Also, the output size is O(target)
Time: O(target * stamp): in the worst case we remove only one char, so we need to make two O(stamp) operations [checking and removing] for every character in the string
"""
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def do_match(target, stamp, index):
            # O(stamp) time
            if index + len(stamp) > len(target):
                return False
            stamp_index = 0
            wildcards = 0
            for i in range(index, len(target)):
                if stamp_index >= len(stamp):
                    break
                if target[i] != '?' and target[i] != stamp[stamp_index]:
                    return False
                if target[i] == '?':
                    wildcards += 1
                stamp_index += 1
            return stamp_index == len(stamp) and wildcards != len(stamp)
        
        def replace(target, stamp, index):
            # returns the number of characters that are modified, and modifies the target
            modified_chars = 0
            for i in range(index, index + len(stamp)):
                if target[i] != '?':
                    modified_chars += 1
                    target[i] = '?'
            return modified_chars
        
        number_of_wildcards = 0
        can_replace = True
        result = []
        target = list(target)
        while can_replace and number_of_wildcards < len(target):
            can_replace = False
            for i in range(len(target) - len(stamp) + 1):
                if do_match(target, stamp, i):
                    can_replace = True
                    modified_chars = replace(target, stamp, i)
                    number_of_wildcards += modified_chars
                    result.append(i)
                    break
        return list(reversed(result)) if can_replace else []
            