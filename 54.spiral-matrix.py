#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        col, row = 0, 0
        result = []
        for i in range(n * n):
            while row < n - i:
                result.append(matrix[col][row])
                row += 1
            while col < n - i:
                result.append(matrix[col][row])
                col += 1
            while row > i:
                result.append(matrix[col][row])
                row -= 1
            while col > i+1:
                result.append(matrix[col][row])
                col -= 1
        return result

