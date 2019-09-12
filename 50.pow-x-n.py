#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n, x = -n, 1/x
        res, i = x, 1
        while i + i <= n:
            res = res * res
            i += i
        for j in range(n-i):
            res = res * x
        return res
        
        

