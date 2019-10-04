# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:12:24 2019

@author: kenzo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        res = ListNode(None)
        node = res
        for i in ans[::-1]:
            node.next = ListNode(i)
            node = node.next
        return res.next
'''

# Reverse Pointer 
class Solution(object):
    def reverseList(self, head):
        rev = None
        while head != None:
            rev, rev.next, head = head, rev, head.next
        return rev
		