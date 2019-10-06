#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
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
            equal = False
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                equal = True
            
            if equal:
                pre.next = cur.next
            else:
                pre = cur

            cur = cur.next
        return result.next
        
# @lc code=end

