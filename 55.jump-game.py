#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for i in range(len(nums)-1):
            max_len = max(max_len, i+nums[i])
            if i == max_len:
                return False
            if max_len >= len(nums)-1:
                return True
        return True
