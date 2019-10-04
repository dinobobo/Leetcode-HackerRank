# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:11:46 2019

@author: kenzo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = {}
        while head != None:
            if head in seen.keys():
                return True
            seen[head] = 0
            head = head.next
        return False
'''
    
#Two pointer
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while (fast != slow):
            if fast == None or fast.next == None:
                return False
            else:
                fast = fast.next.next
                slow = slow.next
        return True