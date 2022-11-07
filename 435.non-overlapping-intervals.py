#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                count += 1
                intervals[i+1][1] = intervals[i][1]

        return count

# @lc code=end
