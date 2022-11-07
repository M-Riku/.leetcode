#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub_seq = []

        def backtracking(start_idx: int):
            if len(sub_seq) >= 2:
                result.append(sub_seq[:])
            if start_idx == len(nums):
                return

            usage_list = set()
            for i in range(start_idx, len(nums)):
                n = nums[i]

                if len(sub_seq) >= 1 and n < sub_seq[-1]:
                    continue

                if n in usage_list:
                    continue

                usage_list.add(n)
                sub_seq.append(n)
                backtracking(i+1)
                sub_seq.pop()

        backtracking(0)
        return result
# @lc code=end
