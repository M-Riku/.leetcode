#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countCompleteNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = right = root
        left_count = right_count = 0
        while left.left:
            left = left.left
            left_count += 1

        while right.right:
            right = right.right
            right_count += 1

        if left_count == right_count:
            return 2 ** (left_count+1) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        nodes_count = self.countCompleteNodes(root)
        return nodes_count

# @lc code=end
