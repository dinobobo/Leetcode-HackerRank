# -*- coding: utf-8 -*-
from collections import deque

class TreeNode(object):
    def __init__(self, x):         
        self.val = x
        self.left = None
        self.right = None
        
        
        
        
        
        
class tree_convert():        
    def tree_construct(self, arr, i):
        if i < len(arr):
            if arr[i]:
                node = TreeNode(arr[i])
                node.left = self.tree_construct(arr, self.left_child(i))
                node.right = self.tree_construct(arr, self.right_child(i))
            else:
                node = None
            return node            
                    
    
    def tree2array(self, root):
        arr = []
        tree_q = deque([root])       
        while tree_q:
            node  = tree_q.popleft()
            if node:
                arr.append(node.val)
                if node.left or node.right:
                    tree_q.append(node.left)
                    tree_q.append(node.right)
            else:
                arr.append(None)
        return arr
    
    
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    
test = tree_convert()
root = test.tree_construct([1,2,3,None, 1,5],0)
arr = test.tree2array(root)
                

