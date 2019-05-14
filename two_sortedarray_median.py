# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:17:20 2019

@author: DinoBob
"""
from math import ceil
class Solution(object):        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m , n = len(nums1),  len(nums2)
        if m > n:
            m , n, num1, num2 = n, m, num2, num1       
        l, r, mid = 0, m - 1, int(m/2)
        j = ceil((m + n)/2)
        while l < r:
            if (i == 0 or j == n or num1[i - 1] <= num2[j]) and (i == m or j == 0 or num1[i] >= num2[j-1]):
                return 
            
        