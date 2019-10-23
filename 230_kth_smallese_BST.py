# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:35:44 2019

@author: kenzo
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from heapq import heappush, heappop

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """ 
        self.hp = []
        self.k = k
        return self.kth_helper(root) 
    def kth_helper(self, root):
        if root:
            self.kth_helper(root.left)
            heappush(self.hp, root.val)
            self.k -= 1
            if self.k == 0:
                return heappop(self.hp)
            self.kth_helper(root.right)
            
        
         

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

x = Solution().kthSmallest(root, 1)