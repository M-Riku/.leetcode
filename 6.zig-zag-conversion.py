#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows <= 1:
            return s
        res = ""
        for i in range(numRows):
            tmp = i
            res += s[tmp]
            inter = [2 * (numRows - i - 1), 2 * i]
            j = 0
            while(tmp + inter[j]< len(s)):
                if(inter[j] == 0):
                    j = 1 - j
                    continue
                tmp += inter[j]
                res += s[tmp]
                j = 1 - j
        return res


