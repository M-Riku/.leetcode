#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def cur(sol, cur_cand, cur_tar):
            if cur_tar == 0:
                result.append(sol)
            elif cur_tar > 0:
                for j in range(len(cur_cand)):
                    i = cur_cand[j]
                    if cur_tar - i < 0:
                        continue
                    else:
                        next_cand = cur_cand.copy()
                        next_cand.remove(i)
                        cur(sol + [i], next_cand, cur_tar - i)

        def remove_duplicate(res):
            hash_res = set()
            for l in res:
                l.sort()
                hash_res.add(tuple(l))
            res = []
            for l in hash_res:
                res.append(list(l))
            return res

        result = []
        cur([], candidates, target)
        result = remove_duplicate(result)
        return result

