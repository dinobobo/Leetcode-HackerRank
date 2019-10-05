# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head 
        
        
        sentinel = ListNode(0)
        sentinel.next = head
        node = sentinel
        
        
        
        while node.next and node.next.next:
            node.next, node.next.next, node.next.next.next = node.next.next, node.next, node.next.next.next
            node = node.next.next            
        return sentinel.next