#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        tmp = 1
        while(l1):
            num1 += l1.val * tmp
            tmp *= 10
            l1 = l1.next
        tmp = 1
        while(l2):
            num2 += l2.val * tmp
            tmp *= 10
            l2 = l2.next
        num = num1 + num2
        dummy = l = ListNode(-1)
        tmp = 10
        while(True):
            l.next = ListNode(int(num % tmp / tmp * 10))
            num -= num % tmp
            tmp *= 10
            l = l.next
            if(num == 0):
                break
        return dummy.next

