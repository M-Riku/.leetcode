#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

## method 1: Brute Force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         container = 0
#         for i, n in enumerate(height):
#             for j, m in enumerate(height[i:]):
#                 tmp = min(n, m) * (j)
#                 if tmp > container:
#                     container = tmp
#         return container

class Solution:
    def maxArea(self, height: List[int]) -> int:
        container = 0
        start = 0
        end = len(height) - 1
        while(start != end):
            if(height[start] >= height[end]):
                tmp = height[end] * (end - start)
                end -= 1
            else:
                tmp = height[start] * (end - start)
                start += 1
            if tmp > container:
                container = tmp
        return container

