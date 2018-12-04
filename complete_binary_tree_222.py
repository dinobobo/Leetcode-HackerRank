# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:29:00 2018

@author: DinoBob
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if self.ctlayer(root.left) == self.ctlayer(root.right):
            return pow(2,self.ctlayer(root.left)) + self.countNodes(root.right) 
        else: 
            return self.countNodes(root.left) + pow(2, self.ctlayer(root.right))
            
    def ctlayer(self, root):
        if not root:
            return 0
        return self.ctlayer(root.left) + 1