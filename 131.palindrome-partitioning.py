#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        pattern = []

        def is_padlindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False

            return True

        def backtracking(start_idx):
            if start_idx >= len(s):
                result.append(pattern[:])
                return

            for i in range(start_idx, len(s)):
                sub_s = s[start_idx:i+1]
                if not is_padlindrome(sub_s):
                    continue
                pattern.append(sub_s)
                backtracking(i+1)
                pattern.pop()

        backtracking(0)
        return result
# @lc code=end
