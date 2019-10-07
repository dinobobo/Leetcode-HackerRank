# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:30:11 2019

@author: DinoBob
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        x = set(nums1)
        y = set(nums2)
        return list(x & y)
        