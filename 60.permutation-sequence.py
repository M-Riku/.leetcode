#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ""
        numbers = [i + 1 for i in range(n)]
        num = 1
        for i in range(1, n):
            num *= i
        for i in  reversed(range(1, n)):
            result += str(numbers.pop((k + num - 1) // num - 1))
            k %= num
            if k == 0:
                k = num
            num = num // i
        result += str(numbers[0])
        return result
# @lc code=end

