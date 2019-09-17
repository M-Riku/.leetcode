#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        pos = [0] * (n1 + n2)
        for i in range(n1)[::-1]:
            for j in range(n2)[::-1]:
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                s = mul + pos[i + j + 1]
                pos[i + j] += s // 10
                pos[i + j + 1] = s % 10
        print(pos)
        result = ""
        for i in range(len(pos)):
            if ( i == 0 and pos[i] == 0):
                continue
            result += str(pos[i])

        return result

