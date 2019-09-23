#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        i, j = len(a), len(b)
        n = max(i, j) - 1
        if i < j:
            a = '0' * (j - i) + a
        else:
            b = '0' * (i - j) + b

        while n > -1:
            s = int(a[n]) + int(b[n]) + carry
            if s >= 2:
                res = str(s % 2) + res
                carry = 1
            else:
                res = str(s % 2) + res
                carry = 0
            n -= 1
            
        if carry == 1:
            res = str(carry) + res
        
        return res
        

