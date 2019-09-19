#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        m, n = len(matrix), len(matrix[0])
        result = []
        loop = (min(m,n)+1) // 2
        flag = True
        for i in range(loop):
            col, row = i, i- 1 
            while row < n - i - 1:
                row += 1
                result.append(matrix[col][row])
                flag = True
            if not flag:
                break
            flag = False
            while col < m - i - 1:
                col += 1
                result.append(matrix[col][row])
                flag = True
            if not flag:
                break
            flag = False
            while row > i:
                row -= 1
                result.append(matrix[col][row])
                flag = True
            if not flag:
                break
            flag = False
            while col > i + 1:
                col -= 1
                result.append(matrix[col][row])
                flag = True
            if not flag:
                break
            flag = False
        return result

