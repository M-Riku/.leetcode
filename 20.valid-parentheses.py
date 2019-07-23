#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for p in s:
            if p not in dic.keys():
                stack.append(p)
            else:
                if not stack:
                    return False
                if stack.pop() != dic[p]:
                    return False
        return not stack

