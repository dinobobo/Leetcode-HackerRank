# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 07:30:51 2019

@author: kenzo
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def generateTrees(self, n):
        nodes = [TreeNode(i) for i in range(1, n+1)]
        return self.make_tree(nodes)
        
    def make_tree(self, nodes):
        if len(nodes) == 0:
            return [None]
        elif len(nodes) == 1:
            return [nodes[0]]
        else:
            ans = []
            for i in range(len(nodes)):
                nodes_l = nodes[:i]
                nodes_r = nodes[i+1:]
                for j in self.make_tree(nodes_l):
                    for k in self.make_tree(nodes_r):
                        node = TreeNode(i + 1)
                        node.left = j
                        node.right = k
                        ans.append(node)
            return ans

        
ans = Solution()
x = ans.generateTrees(3)