# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:34:08 2019

@author: DinoBob
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        pos_idx = self.find_pos_idx(A)
        if pos_idx == None:
            pos_idx = len(A) - 1
        i = pos_idx - 1
        j = pos_idx
        while i >=0 and j < len(A):
            if abs(A[i]) >= abs(A[j]):
                ans.append(abs(A[j])**2)
                j += 1
            else:
                ans.append(abs(A[i]**2))
                i -= 1
        if i < 0:
            ans += [x**2 for x in A[j:]]
        else:
            ans += [x**2 for x in A[:i+1][::-1]]
        return ans
    
    def find_pos_idx(self, A):
        for i in range(len(A)):
            if A[i] >= 0:
                return i
    
ans = Solution()
x = ans.sortedSquares([0,1,3,5])