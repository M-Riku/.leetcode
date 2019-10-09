#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def C(r, n):
            upper = lower = 1
            for x in range(n):
                upper *= (x+1)
            for x in range(r):
                lower *= (x+1)
            for x in range(n-r):
                lower *= (x+1)
            return (upper // lower)

        i, j = 0, n
        count = 0
        while i <= j:
            count += C(i, j)
            i += 1
            j -= 1

        return count
        
# @lc code=end

