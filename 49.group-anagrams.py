#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count not in list(res.keys()):
                res[count] = [s]
            else:
                res[count].append(s)
        result = []
        for r in res.values():
            result.append(r)
        return result
        

