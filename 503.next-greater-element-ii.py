#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        st = []
        for i in range(2*len(nums)):
            cur_i = i % len(nums)
            cur_num = nums[cur_i]
            while st and nums[st[-1]] < cur_num:
                pop_idx = st.pop()
                result[pop_idx] = cur_num
            st.append(cur_i)

        return result
# @lc code=end
