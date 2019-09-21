# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:15:26 2019

@author: kenzo
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = 0
        while j < len(A):
            if A[j] % 2 == 0:
                A[j], A[i] = A[i], A[j]
                i += 1
            j += 1
        return A