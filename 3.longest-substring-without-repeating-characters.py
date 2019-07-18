#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start = length = 0
        for index, c in enumerate(s):
            if c in dict and start <= dict[c]:
                length_tmp = index - dict[c]
                start = dict[c] + 1
            else:
                length_tmp = index - start + 1
            if (length_tmp > length):
                length = length_tmp
            dict[c] = index
        return length

