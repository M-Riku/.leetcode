#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dig_max_idx = {}
        result = []

        for i in range(len(s)):
            dig = s[i]
            dig_max_idx[dig] = i

        max_idx = 0
        last_idx = -1
        for i in range(len(s)):
            dig = s[i]
            max_idx = max(max_idx, dig_max_idx[dig])
            if i == max_idx:
                result.append(max_idx - last_idx)
                last_idx = max_idx

        return result

# @lc code=end
