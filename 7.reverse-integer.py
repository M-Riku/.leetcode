#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if s[-1] == "-":
            s = s[-1] + s[:-1]
        res = int(s)
        if res >= 2**31-1 or res <= -2**31 :
            return 0
        return res

