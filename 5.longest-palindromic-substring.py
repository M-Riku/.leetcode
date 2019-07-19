#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(res) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res


