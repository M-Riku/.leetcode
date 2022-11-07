#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_count = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candy_count[i+1] += 1

        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candy_count[i-1] = max(candy_count[i-1], candy_count[i]+1)

        return sum(candy_count)
# @lc code=end
