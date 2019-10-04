class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next
                
            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA