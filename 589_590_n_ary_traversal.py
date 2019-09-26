# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 06:26:06 2019

@author: kenzo
"""

from collections import deque

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

'''
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        if root:
            ans.append(root.val)
            if root.children:
                for i in root.children:
                    ans += self.preorder(i)
        return ans
'''
#Using queue
class Solution(object):
    def preorder(self, root):
        tree_q = deque([root])
        ans = []
        while tree_q:
            node = tree_q.popleft()
            if node:
                ans.append(node.val)
                if node.children:
                    tree_q += node.children
        return ans
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stk = [root]
        ans = []
        while stk:
            node = stk.pop()
            if node:
                ans.append(node.val)
                if node.children:
                    stk += node.children
        return ans[::-1]