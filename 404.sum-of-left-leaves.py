#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSum(self, node: TreeNode, is_left: bool) -> int:
        if not node:
            return 0

        left_sum = 0
        if node.left:
            left_sum = self.getSum(node.left, True)

        right_sum = 0
        if node.right:
            right_sum = self.getSum(node.right, False)

        if not node.left and not node.right and is_left:
            return node.val

        return left_sum + right_sum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = self.getSum(root, False)
        return result

# @lc code=end
