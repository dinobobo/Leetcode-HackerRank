# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 07:44:20 2019

@author: kenzo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel  = ListNode(0)
        sentinel.next = head
        self.find_lvl(sentinel, n)
        return sentinel.next
    
    def find_lvl(self, head, n):
        if head == None:
            return 0
        node_lvl = self.find_lvl(head.next, n) + 1
        if node_lvl == n + 1:
            head.next = head.next.next
        return node_lvl

test = x = ListNode(1)
for i in range(2,6):
    x.next = ListNode(i)
    x = x.next
x.next = None

ans = Solution().removeNthFromEnd(test, 2)