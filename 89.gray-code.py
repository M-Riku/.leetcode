#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            l = len(result)
            for j in range(l):
                result.append(result[l-1-j] + 2 ** i)
        return result
# @lc code=end

