#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub_set = []

        def backtracking(start_idx):
            result.append(sub_set[:])
            if start_idx == len(nums):
                return

            for i in range(start_idx, len(nums)):
                n = nums[i]

                sub_set.append(n)
                backtracking(i+1)
                sub_set.pop()

        backtracking(0)
        return result

# @lc code=end
