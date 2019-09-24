# -*- coding: utf-8 -*-
from collections import deque

class TreeNode(object):
    def __init__(self, x):         
        self.val = x
        self.left = None
        self.right = None
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
    
test = tree_convert()
root = test.tree_construct([1,2,3,None, 1,5])
arr = test.tree2array(root)
                

