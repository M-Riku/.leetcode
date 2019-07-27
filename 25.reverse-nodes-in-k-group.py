#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverseListNode(head):
            cur_head = None
            while(head != None):
                next = head.next
                head.next = cur_head
                cur_head = head
                head = next
            return cur_head

        if (head == None):
            return None
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        sub_head = toNull = head
        while( sub_head != None):
            for i in range(k-1):
                toNull = toNull.next
                if toNull == None:
                    return dummy.next
            tmp = toNull.next
            toNull.next = None
            new_sub_head = reverseListNode(sub_head)
            tail.next = new_sub_head
            tail = sub_head
            sub_head = tmp
            toNull = sub_head
            tail.next = sub_head
        return dummy.next

