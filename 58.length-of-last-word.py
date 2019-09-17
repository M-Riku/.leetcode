#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)
        while True:
            i -= 1
            if i < 0 or s[i] != " ":
                break
        j = i
        count = 0
        while True:
            if j < 0 or s[j] == " ":
                break
            count += 1
            j -= 1
        return count

