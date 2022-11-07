#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.getHeight(root.left)
        if left_height == -1:
            return -1
        right_height = self.getHeight(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        height = 1 + max(left_height, right_height)
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True if self.getHeight(root) != -1 else False
        return is_balanced
# @lc code=end
