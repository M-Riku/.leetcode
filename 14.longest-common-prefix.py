#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        prefix = strs[0]
        for str in strs[1:]:
            if (prefix == "" or str == ""):
                return ""
            i = 0
            while(prefix[i] == str[i]):
                i += 1
                if (i >= min(len(prefix), len(str))):
                    break
            prefix = prefix[:i]
            
        return prefix

