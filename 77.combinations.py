#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        pattern = []

        def backtracking(start_index: int):
            if len(pattern) >= k:
                result.append(pattern[:])
                return

            for i in range(start_index, n+1):
                pattern.append(i)
                backtracking(i+1)
                pattern.pop()

        backtracking(1)
        return result
# @lc code=end
