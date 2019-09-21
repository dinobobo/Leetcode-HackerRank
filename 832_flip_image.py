# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 07:27:44 2019

@author: kenzo
"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = [~x + 2 for x in A[i][::-1]]
        return A