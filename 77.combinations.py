#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recur(com, ind, k):
            if k == 0:
                result.append(com)
            else:
                tmp = ind
                for i in nums[tmp:]:
                    ind += 1
                    recur(com+[i], ind, k-1)
        
        nums = [x+1 for x in range(n)]
        result = []
        recur([], 0, k)
        return result

# @lc code=end

