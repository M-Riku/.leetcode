#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        head_back = pre = ListNode(-1)
        pre.next = head
        while(head):
            tmp = pre.next
            pre.next = pre.next.next
            tmp.next = tmp.next.next
            pre.next.next = tmp
            pre = pre.next.next
            if not pre.next:
                break
            if not pre.next.next:
                break
        return head_back.next

