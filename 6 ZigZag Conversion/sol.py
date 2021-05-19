"""
How many letters per row? once placed one letter, we have to reach the bottom, go back up until the top and go down again to the same row.
First and last column will only have vertical letters, while the middle rows will also have the diagonals.
If row == 0 or row is last:
- go ahead of 2 * (numRows - 1) until the index is in the string
Middle rows:
- place a letter, go ahead by #rows - current row - 1, go ahead by #rows - current row - 1, place a letter,
go ahead by current row * 2

Corner cases: #rows == 1 or #rows >= len(string), return string.

O(N) time, O(N) space
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        string = []
        for row in range(numRows):
            current_pos = row
            string.append(s[current_pos])
            while current_pos < len(s):
                if row == 0 or row == numRows - 1:
                    current_pos += 2 * (numRows - 1)
                    if current_pos >= len(s):
                        break
                    string.append(s[current_pos])
                else:
                    current_pos += 2 * (numRows - 1 - row)
                    if current_pos >= len(s):
                        break
                    string.append(s[current_pos])
                    current_pos += 2 * row
                    if current_pos >= len(s):
                        break
                    string.append(s[current_pos])
        return "".join(string)
