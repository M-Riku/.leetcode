#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        while (n > 0):
            if nums[n] > nums[n - 1]:
                break
            n -= 1
        n -= 1
        if n >= 0:
            m = n + 1
            while (nums[m] > nums[n]):
                m += 1
                if (m >= len(nums)):
                    break
            m -= 1
            nums[m], nums[n] = nums[n], nums[m]

        left = n + 1
        right = len(nums) - 1
        while(right > left):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

