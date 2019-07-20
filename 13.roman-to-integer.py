#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman_num = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        i = 0
        while(i < len(s)):
            if s[i:i+2] in roman_num.keys():
                num += roman_num[s[i:i+2]]
                i += 2
            else:
                num += roman_num[s[i]]
                i += 1
        return num

