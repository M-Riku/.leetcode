#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for row in range(n)]
        loop = (n + 1) // 2
        m = 0
        for i in range(loop):
            col, row = i, i- 1 
            while row < n - i - 1:
                row += 1
                m += 1
                result[col][row] = m
            while col < n - i - 1:
                col += 1
                m += 1
                result[col][row] = m
            while row > i:
                row -= 1
                m += 1
                result[col][row] = m
            while col > i + 1:
                col -= 1
                m += 1
                result[col][row] = m
        return result   

