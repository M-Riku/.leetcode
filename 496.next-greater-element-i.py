#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)

        st = []
        for i in range(len(nums2)):
            cur_num = nums2[i]
            while st and nums2[st[-1]] <= cur_num:
                pop_num = nums2[st.pop()]
                if pop_num in nums1:
                    result[nums1.index(pop_num)] = cur_num
            st.append(i)

        return result
# @lc code=end
