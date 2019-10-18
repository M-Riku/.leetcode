#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i, j = 0, 1
        result = []
        while j < len(intervals):
            is_merge = False
            while j < len(intervals) and intervals[j][0] <= intervals[j-1][1]:
                j += 1
                is_merge = True

            if is_merge:
                result.append([intervals[i][0], intervals[j-1][1]])
                i = j
                j += 1
            else:
                result.append(intervals[i])
                i == j
                j += 1
        if j == len(intervals):
            result.append(intervals[-1])
        
        return result
# @lc code=end

