"""
We need to scan the board, and when the current cell is equal to the first letter of the word, we start a DFS from the current position guided by the word.
If we reach the end of the word, it means that the word is contained, otherwise if we reach the end of the board and no visits are successful, it means that the word is not contained.

O(NM*3^W) time, O(W)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_neighbours(board, row, col):
            neighbours = []
            if row - 1 >= 0:
                neighbours.append((row - 1, col))
            if row + 1 < len(board):
                neighbours.append((row + 1, col))
            if col - 1 >= 0:
                neighbours.append((row, col - 1))
            if col + 1 < len(board[row]):
                neighbours.append((row, col + 1))
            return neighbours
        
        def dfs(board, row, col, word_index, word, visited):
            if word_index == len(word) - 1:
                return True
            neighbours = get_neighbours(board, row, col)
            for next_row, next_col in neighbours:
                if (next_row, next_col) not in visited and board[next_row][next_col] == word[word_index + 1]:
                    visited.add((next_row, next_col))
                    if dfs(board, next_row, next_col, word_index + 1, word, visited):
                        return True
                    visited.remove((next_row, next_col))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if dfs(board, row, col, 0, word, {(row, col)}):
                        return True
        return False