#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        depth = 1 + max(left_depth, right_depth)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_size = 0
        # if not root:
        #     return max_size

        # from collections import deque
        # queue = deque([root])
        # while queue:
        #     max_size += 1
        #     queue_size = len(queue)
        #     for _ in range(queue_size):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        max_size = self.getDepth(root)

        return max_size

# @lc code=end
