"""
stack to keep track of where we are
when we meet a child directory of our current directory, we push the directory to the stack
when we need to go back (../), we pop the last element from the stack.

O(N) time and space
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sub_path = path.split('/')
        for directory in sub_path:
            if directory == '..' and len(stack) > 0:
                del stack[-1]
            elif directory == '.':
                pass
            elif len(directory) > 0 and directory != '..':
                stack.append(directory)
        return '/' + '/'.join(stack)