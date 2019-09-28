# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:40:24 2019

@author: kenzo
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            depth = 0
            for i in root.children:
                depth = max(self.maxDepth(i), depth)
        else:
            return 0
        return depth + 1