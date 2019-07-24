#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while(right >= left):
            if(nums[left] != val):
                left += 1
            else:
                if(nums[right] != val):
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return left

