#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        result = pre
        cur = head
        while(cur and cur.next):
            while(cur.next and cur.val == cur.next.val):
                cur = cur.next
            
            pre.next = cur
            pre = pre.next
            cur = cur.next
        return result.next
# @lc code=end

