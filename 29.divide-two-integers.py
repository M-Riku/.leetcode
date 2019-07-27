#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            symbol = -1
        else:
            symbol = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend >= divisor):
            dividend -= divisor
            res += 1
        if symbol >= 0:
            return res
        else:
            return -res

