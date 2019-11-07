#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recur(com, ind, k):
            if k == 0:
                result.append(com)
            else:
                tmp = ind
                for i in nums[tmp:]:
                    ind += 1
                    recur(com+[i], ind, k-1)
        
        result = []
        for k in range(len(nums)+1):
            recur([], 0, k)
        return result
# @lc code=end

