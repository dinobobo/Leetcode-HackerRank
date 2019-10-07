# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:57:37 2019

@author: DinoBob
"""

from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        x = defaultdict(int)
        if len(nums1) < len(nums2):
            s = nums1
            l = nums2
        else:
            s = nums2
            l = nums1
            
        for i in s:
            x[i] += 1
        
        ans = []
        for j in l:
            if j in x.keys() and x[j] > 0:
                x[j] -= 1
                ans.append(j)
        return ans
                