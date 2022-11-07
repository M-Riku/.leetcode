#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -10**9
        count = 0
        for right in range(len(nums)):
            count += nums[right]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result
