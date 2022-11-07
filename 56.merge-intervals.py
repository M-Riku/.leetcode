#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                result.append([left, right])
                left = intervals[i+1][0]
            right = intervals[i+1][1]
        result.append([left, right])
        return result
# @lc code=end
