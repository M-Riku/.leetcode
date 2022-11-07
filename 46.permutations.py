#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        pattern = []
        used_list = [False] * len(nums)

        def backtracking(used_list: List):
            if len(pattern) == len(nums):
                result.append(pattern[:])
                return

            for i in range(len(nums)):
                if used_list[i]:
                    continue

                pattern.append(nums[i])
                used_list[i] = True
                backtracking(used_list)
                used_list[i] = False
                pattern.pop()

        backtracking(used_list)
        return result
