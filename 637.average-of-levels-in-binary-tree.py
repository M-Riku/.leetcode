#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return result

        from collections import deque
        queue = deque([root])
        while queue:
            total = 0
            queue_size = len(queue)
            for _ in range(queue_size):
                cur = queue.popleft()
                total += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ave = total / queue_size
            result.append(ave)

        return result
# @lc code=end
