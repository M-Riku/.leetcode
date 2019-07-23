#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        
        tail = cur = head
        for i in range(n):
            tail = tail.next
        if tail == None:
            return head.next

        while(tail.next):
            tail = tail.next
            cur = cur.next
        cur.next = cur.next.next
        return head

