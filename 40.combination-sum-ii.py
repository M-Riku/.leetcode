#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        pattern = []
# 1 1 2 5 6 7 10

        def backtracking(start_idx: int, cur_sum: int):
            if cur_sum == target:
                result.append(pattern[:])
                return

            for i in range(start_idx, len(candidates)):
                n = candidates[i]
                if cur_sum + n > target:
                    return

                if i > start_idx and n == candidates[i-1]:
                    continue
                cur_sum += n
                pattern.append(n)
                backtracking(i+1, cur_sum)
                cur_sum -= n
                pattern.pop()

        candidates.sort()
        backtracking(0, 0)
        return result
