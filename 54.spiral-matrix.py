#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
        m, n = len(matrix), len(matrix[0])
        result = []
        loop = min(m,n) // 2
        for i in range(loop):
            col, row = i, i- 1 
            while row < n - i - 1:
                row += 1
                print(col, row)
                result.append(matrix[col][row])
            while col < m - i - 1:
                col += 1
                print(col, row)
                result.append(matrix[col][row])
            while row > i:
                row -= 1
                print(col, row)
                result.append(matrix[col][row])
            while col > i + 1:
                col -= 1
                print(col, row)
                result.append(matrix[col][row])
        return result

