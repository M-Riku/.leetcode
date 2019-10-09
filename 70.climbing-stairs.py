#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def curClimb(cur, way):
            if cur == 0:
                result.append(way)
            else:
                if cur > 1:
                    curClimb(cur - 2, way + [2])
                curClimb(cur - 1, way + [1])

        result = []
        curClimb(n, [])
        return len(result)
        
# @lc code=end

