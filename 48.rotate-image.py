#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(len(matrix)//2):
            for j in range(i,n-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = tmp


