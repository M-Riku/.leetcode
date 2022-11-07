#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_dict = {}
        for i in nums:
            freq_dict[i] = freq_dict.get(i, 0) + 1

        freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(freq_dict[i][0])
        return result
# @lc code=end
