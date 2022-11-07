#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node: TreeNode) -> int:
        if not node:
            return 0

        if not node.left and not node.right:
            return 1

        min_depth = 10 ** 9
        if node.left:
            min_depth = min(min_depth, self.getDepth(node.left))

        if node.right:
            min_depth = min(min_depth, self.getDepth(node.right))
        return min_depth + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = self.getDepth(root)
        return min_depth
# @lc code=end
