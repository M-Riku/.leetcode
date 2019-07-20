#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def getStartIndex(self, s: str) -> int: 
        start_index = 0
        for c in s:
            if c == " ":
                start_index += 1
            else:
                break
        return start_index

    def myAtoi(self, str: str) -> int:
        result = "0"

        if str == "":
            return 0
        start = self.getStartIndex(str)

        if start >= len(str):
            return 0

        if str[start].isalpha():
            return 0

        sign = str[start] in ["-", "+"]
        if sign and len(str) == 1:
            return 0

        if sign:
            result = str[start] + result
            start += 1
        for c in range(start, len(str)):
            if not str[c].isnumeric():
                break
            result += str[c]

        result = int(result)
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31 :
            return -2**31
        return result


