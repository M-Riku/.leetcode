#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        fast = head
        slow = ListNode(-1)
        slow.next = head
        for i in range(length-k):
            fast = fast.next
            slow = slow.next
        tail.next = head
        slow.next = None
        return fast
# @lc code=end

