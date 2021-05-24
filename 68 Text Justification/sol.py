"""
start_index, final_index => the first and the last word I'm gonna put on the current line
current_len => the sum of the lengths of the words I'm considering to add to the current line
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def store_line(words, maxWidth, current_line, result):
            if len(current_line) == 1:
                res = " ".join(current_line)
                spaces_to_add = maxWidth - len(res)
                for _ in range(spaces_to_add):
                    res += " "
                result.append(res)
            else:
                spaces_to_add = maxWidth - sum([len(x) for x in current_line])
                spaces_between_words = spaces_to_add / (len(current_line) - 1) if len(current_line) > 1 else 0
                total_space = maxWidth
                res = ""
                for i in range(len(current_line)):
                    w = current_line[i]
                    res += w
                    total_space -= len(w)
                    if i < len(current_line) - 1 and total_space >= int(spaces_between_words) + len(current_line[i + 1]):
                        spaces = int(spaces_between_words)
                        if spaces_between_words - spaces >= 0.5 and total_space - spaces - 1 - len(current_line[i + 1]) >= 0:
                            spaces += 1
                        res += " " * spaces
                        total_space -= spaces
                result.append(res)
        
        result = []
        start_index = 0
        final_index = 0
        current_len = 0
        current_line = []
        for word in words:
            len_with_spaces = current_len + len(current_line)
            if not current_line:
                current_line.append(word)
                current_len += len(word)
            elif len_with_spaces + len(word) <= maxWidth:
                current_line.append(word)
                current_len += len(word)
            else:
                # store the row
                store_line(words, maxWidth, current_line, result)
                current_line = [word]
                current_len = len(word)
        res = " ".join(current_line)
        spaces_to_add = maxWidth - len(res)
        for _ in range(spaces_to_add):
            res += " "
        result.append(res)
        return result