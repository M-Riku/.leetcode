#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            tmp = nums[i]
            if target-tmp in dict:
                return [dict[target-tmp], i]
            dict[tmp] = i

