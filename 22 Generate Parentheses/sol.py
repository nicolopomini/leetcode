"""
0: none
1: ()
2: ()() (())
3:()()() ()(())  (()()) (())() ((()))
For each N, 3 possibilities:
Open, close, N - 1
N - 1, open, close
Open, N - 1, close
Pay attention when the base case is ()*, because a duplicate can be generated. It works but we need to check for duplicates. 
It is better to keep track of the number of opened and closed parenthesis.
Pseudocode:
generate(to_open, to_close, current, result)
    If to_open == 0 and to_close == 0
        Add current to result
    If to_open > 0:
        Open a parenthesis and recurse
    If to_close < to_open
        Close a parenthesis and recurse

Recursive calls with n = 3
o = 3, c = 3
    o = 2, c = 3
        o = 1, c = 3
            o = 0, c = 3
                o = 0, c = 2
                    o = 0, c = 1
                        o = 0, c = 0
            o = 1, c = 2
                o = 0, c = 2
                    o = 0, c = 1
                        o = 0, c = 0
                o = 1, c = 1
                    o = 0, c = 1
                        o = 0, c = 0
        o = 2, c = 2
            o = 1, c = 2
                o = 0, c = 2
                    o = 0, c = 1
                        o = 0, c = 0
                o = 1, c = 1
                    o = 0, c = 1
                        o = 0, c = 0
Complexity is O((2N)! / (N! * (N + 1)!))
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(to_open, to_close, current, result):
            if to_open == 0 and to_close == 0:
                result.append("".join(current))
            else:
                if to_open > 0:
                    generate(to_open - 1, to_close, current + ['('], result)
                if to_close > to_open:
                    generate(to_open, to_close - 1, current + [')'], result)
        
        results = []
        generate(n, n, [], results)
        return results
    