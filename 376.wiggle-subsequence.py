#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_diff, cur_diff = 0, 0
        count = len(nums)

        for i in range(len(nums) - 1):
            cur_diff = nums[i+1] - nums[i]
            if cur_diff == 0 or cur_diff * pre_diff > 0:
                count -= 1
            else:
                pre_diff = cur_diff

        return count

# @lc code=end
