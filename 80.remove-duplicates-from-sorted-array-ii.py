#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_index = 1
        count = 1
        for i in range(1, len(nums)):
            if(nums[i] == nums[valid_index-1]):
                count += 1
            else:
                count = 1

            if count > 2:
                continue
            else:
                nums[valid_index], nums[i] = nums[i], nums[valid_index]
                valid_index += 1
        return valid_index
# @lc code=end
