# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:48:53 2019

@author: DinoBob
"""
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rev = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast != None:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
x = Solution().isPalindrome(head)