#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split('/')
        direct = []
        result = ''
        for s in files:
            if s == '' or s == '.':
                continue
            elif s == '..':
                if direct:
                    direct.pop()
                else:
                    pass
            else:
                direct.append(s)
        for s in direct:
            result += '/'
            result += s
        if not result:
            return '/'
        return result
# @lc code=end

