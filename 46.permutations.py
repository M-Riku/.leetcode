#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(cur_res, cur_nums):
            if not cur_nums:
                result.append(cur_res)
            else:
                for i in cur_nums:
                    next_res = cur_res.copy()
                    next_res.append(i)
                    next_nums = cur_nums.copy()
                    next_nums.remove(i)
                    recur(next_res, next_nums)

        result = []
        recur([], nums)
        return result

