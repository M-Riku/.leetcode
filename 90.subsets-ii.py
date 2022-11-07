#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub_set = []

        def backtracking(start_idx: int):
            result.append(sub_set[:])
            if start_idx == len(nums):
                return

            for i in range(start_idx, len(nums)):
                n = nums[i]

                if i > start_idx and n == nums[i-1]:
                    continue

                sub_set.append(n)
                backtracking(i+1)
                sub_set.pop()

        nums.sort()
        backtracking(0)
        return result

# @lc code=end
