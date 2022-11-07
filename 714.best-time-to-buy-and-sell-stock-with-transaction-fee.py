#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_p = max_p = prices[0]
        profit = 0
        for price in prices:
            if max_p - price > fee:
                if max_p - min_p - fee > 0:
                    profit += (max_p - min_p - fee)
                min_p = max_p = price
            min_p = min(min_p, price)
            max_p = max(max_p, price)
        if max_p - min_p - fee > 0:
            profit += (max_p - min_p - fee)
        return profit

# @lc code=end
