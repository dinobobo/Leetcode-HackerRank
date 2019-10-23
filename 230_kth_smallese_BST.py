# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:35:44 2019

@author: kenzo
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        st = deque([])
        ans = []
        while True:
            if root:
                st.append(root)
                root = root.left
            elif(st):
                root = st.pop()
                ans.append(root.val)
                k -= 1
                root = root.right
                if k == 0:
                    return ans[-1]
            
        
         

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

x = Solution().kthSmallest(root, 1)