# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:03:15 2019

@author: kenzo
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        i = j = head
        lvl = 0
        while j != None and lvl < k:
            j = j.next
            lvl += 1       
        if j:
            while j.next != None:
                i = i.next
                j = j.next
            j.next = head
            ans = i.next
            i.next = None
            return ans
        else:
            return self.rotateRight(head, k%lvl)