"""
We have to keep track of the current line we are scanning, and of the fact whether we are in a block comment
The rest is pretty straightforward:
- if we are on a block comment, we have to look for the closing of the comment, and we do not push the line
- otherwise we look for opening comments

We push a line only if it is not empty
O(NL) time and space (N number of lines, L length of the longest line)
"""
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        on_block_comment = False
        current_line = []
        for line in source:
            i = 0
            while i < len(line):
                if on_block_comment:
                    if line[i] == '*' and i < len(line) - 1 and line[i + 1] == '/':
                        i += 1 # skip the / on the next iteration
                        on_block_comment = False
                else:
                    if line[i] == '/' and i < len(line) - 1 and line[i + 1] == '/':
                        break
                    elif line[i] == '/' and i < len(line) - 1 and line[i + 1] == '*':
                        i += 1 # skip the * on the next iteration
                        on_block_comment = True
                    else:
                        current_line.append(line[i])
                i += 1
            if not on_block_comment and current_line:
                result.append("".join(current_line))
                current_line = []
        return result
