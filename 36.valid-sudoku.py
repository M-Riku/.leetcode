#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                num = "(" + board[i][j] + ")"
                row = str(i) + num
                col = num + str(j)
                boa = str(i//3) + num + str(j//3)
                if row in hashset or col in hashset or boa in hashset:
                    return False
                else:
                    hashset.append(row)
                    hashset.append(col)
                    hashset.append(boa)
        return True

