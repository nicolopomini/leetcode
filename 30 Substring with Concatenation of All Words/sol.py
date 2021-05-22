"""
String not empty, words can be repeated.
Brute force: create all the permutations of the words array, and check if any of them is a substring.

Use a sliding window and two data structure to support the algorithm:
- a dictionary to count the appearances of each item of words
- another dictionary to count the appearances of each item of words in the current substring.
Let N be the number of strings in words, and k the length of each string, left the left part of the window and right the right part.
The window can start at any point of the string, so left will try all the indexes between 0 and len(s) - number_of_words * single_word_size (after that there would be no space for a substring).
For every left index, we try to build a substring containing all the words:
- if we meet a word in the string that is not part of the array of words, we can abort the current iteration and go to the next left index
- if we find too many times a word, we can abort the current iteration and go to the next left index
- if we arrive to consume all the words in the words array, we found a solution!

O(N + M) space, where M is the lenght of the main string (the size of the result can be O(M))
O(N * M * k)
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def get_counters(words):
            counters = {}
            for word in words:
                if word not in counters:
                    counters[word] = 0
                counters[word] += 1
            return counters
        
        def add_to_solution(word, current_solution):
            if word not in current_solution:
                current_solution[word] = 0
            current_solution[word] += 1
        
        counters = get_counters(words)
        number_of_words = len(words)
        single_word_size = len(words[0])
        result = []
        left = 0
        right = single_word_size
        
        for left in range(len(s) - number_of_words * single_word_size + 1):
            current_solution = {}   # keeps the counters of the current solution
            for right in range(number_of_words):
                next_word_index = left + right * single_word_size
                word = s[next_word_index: next_word_index + single_word_size]
                if word not in counters:
                    break
                add_to_solution(word, current_solution)
                if current_solution[word] > counters[word]:
                    break
                if right + 1 == number_of_words:
                    result.append(left)
        return result