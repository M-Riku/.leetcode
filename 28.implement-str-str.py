#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        res = -1
        for i in range(len(haystack)-l + 1):
            if haystack[i:i+l] == needle:
                res = i
                break
        return res

