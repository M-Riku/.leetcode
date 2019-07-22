#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        res = []
        while(i < len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                    while(nums[end] == nums[end + 1] and end > i + 1):
                        end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                    while(nums[start] == nums[start-1] and start < len(nums) - 1):
                        start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while(nums[start] == nums[start-1] and start < len(nums) - 1):
                        start += 1
            i += 1
            while( nums[i] == nums[i-1] and i < len(nums)-2):
                i += 1
        return res

