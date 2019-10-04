# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        while head != None and head.val == val:
            head = head.next
            
        node = head
        while node != None and node.next != None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head
'''
class Solution(object):
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, sentinel.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next