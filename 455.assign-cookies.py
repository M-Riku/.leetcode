#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_point = len(g) - 1
        s_point = len(s) - 1
        content = 0
        while g_point >= 0 and s_point >= 0:
            if s[s_point] >= g[g_point]:
                content += 1
                s_point -= 1

            g_point -= 1

        return content
# @lc code=end
