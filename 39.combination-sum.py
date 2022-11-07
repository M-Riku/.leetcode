#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        pattern = []

        def backtracking(cur_sum, start_index):
            if cur_sum == target:
                result.append(pattern[:])
                return

            if cur_sum > target:
                return

            for i in range(start_index, len(candidates)):
                n = candidates[i]
                pattern.append(n)
                cur_sum += n
                backtracking(cur_sum, i)
                pattern.pop()
                cur_sum -= n

        backtracking(0, 0)
        return result
