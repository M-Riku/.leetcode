#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        point = 0
        while point <= right:
            if nums[point] == 0:
                nums[left], nums[point] = nums[point], nums[left]
                left += 1
            elif nums[point] == 2:
                nums[right], nums[point] = nums[point], nums[right]
                right -= 1
                if nums[point] != 1:
                    continue
            else:
                pass
            point += 1

# @lc code=end

