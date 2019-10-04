# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:11:45 2019

@author: DinoBob
"""

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow