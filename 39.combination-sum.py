#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def cur(sol, cur_tar):
            if cur_tar == 0:
                result.append(sol)
            elif cur_tar > 0:
                if sol:
                    start = candidates.index(sol[-1])
                else:
                    start = 0
                for i in candidates[start:]:
                    if cur_tar - i < 0:
                        break
                    else:
                        cur(sol + [i], cur_tar - i)

        result = []
        candidates.sort()
        cur([], target)
        return result


