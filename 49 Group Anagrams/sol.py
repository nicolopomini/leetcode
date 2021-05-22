"""
Easiest approach: sort each strings, and then use a hashmap to bring them together.
Let N be the number of strings, S be the length of the longest one, the complexity is:
O(N * S * logS) time, O(N*S) space. 

Alternative: Since the alphabet is made of lower-case English letters, we know that every string can be made by 26 characters. We can create an array of 26 elements, each one containing the counter of how many times a character appears. We trnasform each character to its unicode, and we shift it with the unicode of 'a' (in order to have a value between 0 and 26). In this way we create the same string for all the anagrams made by the same letters.
O(NS) time and space
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(string):
            code = [0 for _ in range(26)]
            for c in string:
                code[ord(c) - ord('a')] += 1
            return "-".join([str(c) for c in code])
        
        anagram_groups = {}
        for anagram in strs:
            code = encode(anagram)
            if code not in anagram_groups:
                anagram_groups[code] = []
            anagram_groups[code].append(anagram)
        return list(anagram_groups.values())