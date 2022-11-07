#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 0
        cur_cover = 0
        next_cover = 0
        for i in range(len(nums)-1):
            next_cover = max(next_cover, i+nums[i])
            if i == cur_cover:
                step += 1
                cur_cover = next_cover
        return step
# @lc code=end
