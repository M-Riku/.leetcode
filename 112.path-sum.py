#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcPathSum(self, node: TreeNode, target_sum: int, cur_sum: int) -> bool:
        print(cur_sum)
        if not node.left and not node.right:
            if cur_sum == target_sum:
                return True
            else:
                return False

        if node.left:
            if self.calcPathSum(node.left, target_sum, cur_sum+node.left.val):
                return True

        if node.right:
            if self.calcPathSum(node.right, target_sum, cur_sum+node.right.val):
                return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        result = self.calcPathSum(root, targetSum, root.val)
        return result
# @lc code=end
