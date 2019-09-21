# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:30:27 2019

@author: kenzo
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
        
'''  
#Using stack
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        st = [root]
        while st:
            if st[-1].val == val:
                return st[-1]
            else:
                p = st.pop()
                if p.left:
                    st.append(p.left)
                if p.right:
                    st.append(p.right)
        return