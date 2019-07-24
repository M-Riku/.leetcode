#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
        return i+1

