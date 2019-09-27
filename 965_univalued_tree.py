# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:00:27 2019

@author: kenzo
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            val = root.val
            if root.left:
                if self.isUnivalTree(root.left) and val == root.left.val:
                    pass
                else:
                    return False

            if root.right:
                if self.isUnivalTree(root.right) and val == root.right.val:
                    pass
                else:
                    return False
        return True
    
    