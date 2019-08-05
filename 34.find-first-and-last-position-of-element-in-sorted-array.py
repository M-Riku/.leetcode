#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return [res, res]

        start = end = mid
        if start > 0:
            while nums[start] == nums[start - 1]:
                start -= 1
                if start <= 0:
                    break
        if end < len(nums) - 1:
            while nums[end] == nums[end + 1]:
                end += 1
                if end >= len(nums) - 1:
                    break
        return [start, end]

