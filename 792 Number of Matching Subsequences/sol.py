"""
Naive solution: for each word, check if it is a subsequence: O(N*(W + S)) time, O(1) space, where N is the number of words, W is the longest word and S is the length of the string.
Better option: keep a list of N integers, indicating the index of each word that we reached.
Then, for every char in string, increase by one the index of a word if the current index is equal to the character.
When the index of a word is equal to the len of the string, we can add it to the result.
O(S*N) time, O(N) space TLE
Similar approach, using a hashmap char => list of strings, indicating which is the next character that is waited by the list of strings.
Then we scan the string once, moving all the strings that received that letter into their next letter, until all the letters have been consumed.
In that case, we can increase a counter.
O(S + N*W) time, O(N*W) space (since the alphabet size is fixed)
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # waiting_for contains, for each character in the alphabet, a dictionary with keys the word waiting for that char, and value the current char position inside the word
        waiting_for = {}
        # count how many times each word appears, in case of duplicates
        word_counter = {}
        answer = 0
        for char in list('abcdefghijklmnopqrstuvwxyz'):
            waiting_for[char] = {}
        for word in words:
            if word not in word_counter:
                word_counter[word] = 0
            word_counter[word] += 1
            # set the first char of each word in waiting_for
            waiting_for[word[0]][word] = 0
        for char in s:
            # get all the words waiting for the current char
            waiting_for_char = waiting_for.get(char, [])
            # new_words will be the new content of waiting_for[char]
            new_words = {}
            for word in waiting_for_char:
                current_char = waiting_for_char[word]
                if current_char + 1 == len(word):
                    # reach the end of the word, add the number of times it appears to the results
                    answer += word_counter[word]
                elif word[current_char + 1] == word[current_char]:
                    # the next char is equal to the current, this word stays in waiting_for[char]
                    new_words[word] = current_char + 1
                else:
                    # move the word to the list related to the next char
                    waiting_for[word[current_char + 1]][word] = current_char + 1
                waiting_for[word] = new_words
            # replace the current waiting list
            waiting_for[char] = new_words
        return answer