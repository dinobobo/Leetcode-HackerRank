# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 05:53:45 2019

@author: kenzo
"""
from tree_construct import tree_convert
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = self.sum_helper(root)
        ans = 0
        for i in arr:
            for j, k in enumerate(i[::-1]):
                ans += k*(2**j)
        return ans
        
    def sum_helper(self, root):
        ans = []
        if root:
            ans_l = self.sum_helper(root.left)
            ans_r = self.sum_helper(root.right)
            if ans_l and ans_r:
                for i in ans_l:
                    ans.append([root.val] + i)
                for j in ans_r:
                    ans.append([root.val] + j)
            elif ans_l and not ans_r:
                for i in ans_l:
                    ans.append([root.val] + i)
            elif not ans_l and ans_r:
                for j in ans_r:
                    ans.append([root.val] + j)
            else:
                ans.append([root.val])            
        return ans

if __name__ == "__main__":
    test = [1,0,1,0,1,0,1]
    cv = tree_convert()
    root = cv.tree_cons_st(test)
    ans = Solution()
    x = ans.sumRootToLeaf(root)