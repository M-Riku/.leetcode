#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        while (i < len(nums) - 3):
            j = len(nums) - 1
            while (j > 2):
                start = i + 1
                end = j - 1
                while (end > start):
                    x = nums[i] + nums[start] + nums[end] + nums[j]
                    if x > target:
                        end -= 1
                        while(nums[end] == nums[end+1] and end > start):
                            end -= 1
                    elif x < target:
                        start += 1
                        while(nums[start] == nums[start-1] and end > start):
                            start += 1
                    else:
                        res.append([nums[i], nums[start], nums[end], nums[j]])
                        end -= 1
                        while(nums[end] == nums[end+1] and end > start):
                            end -= 1
                j -= 1
                while(nums[j] == nums[j+1] and j > i + 2):
                    j -= 1
            i += 1
            while(nums[i] == nums[i-1] and i < len(nums) - 3):
                i += 1
        return res
                    

