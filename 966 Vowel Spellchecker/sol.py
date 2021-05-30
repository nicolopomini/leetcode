"""
If we were allowed to return any word matching with any rule, we could have used a trie with all the word in wordList, but since we are forced to return the first word that matches a query, we need some order.
The priorities are:
1. exact match
2. capitalization match
3. vowel match

For the exact match we create a hashset of the wordList
For the capitalization match we create a hashmap, with keys the words in lowecase version, and values their real version
For the third one, we can build another hashmap, with keys any vowel replacement of the word in wordList, and values the real version, or in alternative is building on the fly a possible match. We don't need all the replacements, we just replace the vowels with a character not in the alphabet (e.g. '.')
Since the priority must be given to the first word in wordList, the wordList list must be scanned reversed, in order to avoid that two words with the same lowercase version are overriding an already existing key in the hashmaps.
O(W + Q) time, O(W + Q) space
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def remove_vowels(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return "".join(['.' if c in vowels else c for c in word])
            
        
        exact_match = set()
        capitalize_match = {}
        vowel_match = {}
        for word in reversed(wordlist):
            exact_match.add(word)
            lowercase_word = word.lower()
            capitalize_match[lowercase_word] = word
            vowel_match[remove_vowels(lowercase_word)] = word
        
        result = []
        for query in queries:
            query_result = ""
            query_lowercase = query.lower()
            query_lowercase_without_vowels = remove_vowels(query_lowercase)
            if query in exact_match:
                query_result = query
            elif query_lowercase in capitalize_match:
                query_result = capitalize_match[query_lowercase]
            elif query_lowercase_without_vowels in vowel_match:
                query_result = vowel_match[query_lowercase_without_vowels]
            result.append(query_result)
        return result