#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dump_dis = 0
        for i in range(len(nums)):
            if i > dump_dis:
                return False
            dump_dis = max(dump_dis, nums[i] + i)
        return True
        

