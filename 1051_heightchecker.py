# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:16:53 2019

@author: kenzo
"""

from collections import Counter
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights  = [i - j for i, j in zip(heights, sorted(heights))]
        return len(heights) - Counter(heights)[0]