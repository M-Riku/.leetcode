#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        pattern = []

        def backtracking(start_idx):
            if sum(pattern) > n:
                return

            if len(pattern) == k:
                if sum(pattern) == n:
                    result.append(pattern[:])
                return

            for i in range(start_idx, 10):
                pattern.append(i)
                backtracking(i+1)
                pattern.pop()

        backtracking(1)
        return result
# @lc code=end
