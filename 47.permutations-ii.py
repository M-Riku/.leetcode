#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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

        def remove_duplicate(res):
            hash_set = set()
            for l in res:
                hash_set.add(tuple(l))
            res = []
            for l in hash_set:
                res.append(list(l))
            return res

        result = []
        recur([], nums)
        result = remove_duplicate(result)
        return result

