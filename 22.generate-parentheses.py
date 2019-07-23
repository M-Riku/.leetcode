#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recur(stack, letter, n):
            if n == 0:
                while stack:
                    letter += ")"
                    stack.pop()
                res.append(letter)
            else:
                if not stack:
                    stack.append("(")
                    recur(stack.copy(), letter+"(", n-1)
                else:
                    tmp = stack.copy()
                    tmp.append("(")
                    recur(tmp.copy(), letter+"(", n-1)
                    tmp = stack.copy()
                    tmp.pop()
                    recur(tmp.copy(), letter+")", n)
        
        res = []
        recur([], "", n)
        return res

