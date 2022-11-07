#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node: TreeNode, path: str, result: List) -> str:
        if not node:
            return ''

        if not node.left and not node.right:
            result.append(path + str(node.val))

        if node.left:
            self.traversal(node.left, path+str(node.val)+"->", result)

        if node.right:
            self.traversal(node.right, path+str(node.val)+"->", result)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = ''
        result = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
        # @lc code=end
