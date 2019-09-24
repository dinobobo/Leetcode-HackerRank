# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:49:18 2019

@author: DinoBob
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1_q = deque([t1])
            t2_q = deque([t2])
            while t1_q:
                node1 = t1_q.popleft()
                print(node1.val)
                node2 = t2_q.popleft()
                node1.val += node2.val
                if node1.left and node2.left:
                    t1_q.append(node1.left)
                    t2_q.append(node2.left) 
                elif not node1.left and node2.left:
                    node1.left = node2.left
                if node1.right and node2.right:
                        t1_q.append(node1.right)
                        t2_q.append(node2.right)
                elif not node1.right and node2.right:
                    node1.right = node2.right
            return t1
        elif t1 and not t2:
            return t1
        elif t2 and not t1:
            return t2
        else:
            return None
        
        

                    
                
                
class tree_convert():        
    def tree_construct(self, arr):
        if arr:
            root = TreeNode(arr[0])
            tree_q = deque([root])
            i = 0
            while i < len(arr):
                node = tree_q.popleft()
                if arr[i]:
                    if len(tree_q) <= len(arr) - i - 2:
                        node.left = TreeNode(None)
                        tree_q.append(node.left)
                    if len(tree_q) <= len(arr) - i - 2:  
                        node.right = TreeNode(None)
                        tree_q.append(node.right)
                node.val = arr[i]
                i += 1
            return root
    def tree2array(self, root):
        arr = []
        tree_q = deque([root])       
        while tree_q:
            node  = tree_q.popleft()
            if node:
                tree_q.append(node.left)
                tree_q.append(node.right)
                arr.append(node.val)
        return arr
        
t_build = tree_convert()
t1 = t_build.tree_construct([1,3,2,5])
t2 = t_build.tree_construct([2,1,3,None,4,None,7])
ans = Solution()
x = t_build.tree2array(ans.mergeTrees(t1,t2))
