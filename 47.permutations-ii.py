#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        pattern = []
        used_list = [False] * len(nums)

        def backtracking(used_list: List):
            if len(pattern) == len(nums):
                result.append(pattern[:])
                return

            used_set = set()
            for i in range(len(nums)):
                n = nums[i]
                if used_list[i]:
                    continue

                if n in used_set:
                    continue

                used_list[i] = True
                used_set.add(n)
                pattern.append(n)
                backtracking(used_list)
                used_list[i] = False
                pattern.pop()

        nums.sort()
        backtracking(used_list)
        return result
