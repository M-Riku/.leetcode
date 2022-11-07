#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = total_sum = 0
        start_idx = 0
        for i in range(len(gas)):
            res = gas[i] - cost[i]
            cur_sum += res
            total_sum += res
            if cur_sum < 0:
                cur_sum = 0
                start_idx = i+1

        if total_sum < 0:
            return -1

        return start_idx

# @lc code=end
