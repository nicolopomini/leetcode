"""
Basic approach: we have to see if a word in words1 is a superset of all the words in words2. To do so, we have to check that all the characters of a word in word2 appears in word1, and that their couters are greater or equal in word1 with respect to word2.
This property must be valid on all the words in words2.
For this reason we can compact all the words in words2 into a single hashmap, counting all characters appearing in all the words of word2 the largest number of times.
E.g. words2 = ['abc', 'aba'], our counters must be {'a': 2, 'b': 1, 'c': 1}.
Then all the words in words1 that have all the letters in the counter for at least a number of times equal to the one of the counter, they are universal words.

Complexity:
- compacting the words: O(words2 * longest word) time, O(alphabet) space
- finding the universal words: O(words1 +  (longest word in words1 + alphabet)) to count the words and compare the counters with words2, O(alphabet) space
"""
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def get_counter_of_word(word):
            counters = {}
            for c in word:
                if c not in counters:
                    counters[c] = 0
                counters[c] += 1
            return counters
        
        def update_global_counter(global_counter, word_counter):
            for c in word_counter:
                if c not in global_counter:
                    global_counter[c] = word_counter[c]
                else:
                    global_counter[c] = max(word_counter[c], global_counter[c])\
    
        def is_universal(counters, global_counter):
            for c in global_counter:
                if c not in counters:
                    return False
                if counters[c] < global_counter[c]:
                    return False
            return True
        
        global_counter = {}
        for w2 in words2:
            counters = get_counter_of_word(w2)
            update_global_counter(global_counter, counters)
        result = []
        for w1 in words1:
            counters = get_counter_of_word(w1)
            if is_universal(counters, global_counter):
                result.append(w1)
        return result