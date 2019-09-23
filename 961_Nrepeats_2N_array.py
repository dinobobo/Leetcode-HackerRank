# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:49:51 2019

@author: DinoBob
"""

class Solution:
    def repeatedNTimes(self, A):
        i = 0
        while i + 3 < len(A):
            ans = self.find_repeat(A[i: i+4])
            if ans!= None:
                return ans
            i += 4
        if i < len(A):
            return self.find_repeat(A[i:])
            
            
    def find_repeat(self, subA):
        arr = []
        for i in subA:
            if i in arr:
                return i
            else:
                arr.append(i)
        
ans = Solution()
ans.repeatedNTimes([4,1,7,0,0,9,0,0])