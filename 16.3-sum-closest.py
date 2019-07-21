#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sub = 2 ** 31 - 1
        res = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (right > left):
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < sub:
                    sub = abs(sum - target)
                    res = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return res
        return res

