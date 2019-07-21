#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        start = 0
        end = len(nums) - 1
        while(start < end - 1):
            while(end - start > 1):
                x = 0 - nums[start] - nums[end]
                if x in nums[start+1:end]:
                    res.append([nums[start], x, nums[end]])
                while(nums[end] == nums[end-1] and end > 1):
                    end -= 1
                end -= 1
            while(nums[start] == nums[start+1] and start < len(nums)-2):
                start += 1
            start += 1
            end = len(nums) - 1
        return res

