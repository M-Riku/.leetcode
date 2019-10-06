#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print(nums1, nums2)
        for i in range(m):
            nums1[m+n-1-i] = nums1[m-1-i]
        # print(nums1, nums2)
        p = p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1 + n] <= nums2[p2]:
                nums1[p] = nums1[p1 + n]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
            print(nums1, p, p1, p2)
        
        while p2 < n:
            nums1[p] = nums2[p2]
            p += 1
            p2 += 1
        
# @lc code=end

