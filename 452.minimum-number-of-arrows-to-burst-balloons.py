#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        count = 1

        for i in range(len(points)-1):
            if points[i][1] >= points[i+1][0]:
                points[i+1][1] = min(points[i][1], points[i+1][1])
            else:
                count += 1

        return count


# @lc code=end
