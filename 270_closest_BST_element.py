# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:57:01 2019

@author: DinoBob
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        mi = root.val
        while root is not None:
            if abs(root.val - target) < abs(mi - target):
                mi = root.val
            if root.val == target:
                return root.val
            elif root.val > target:
                root = root.left
            else:
                root = root.right
            
        return mi