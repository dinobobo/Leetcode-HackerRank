# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:59:05 2019

@author: kenzo
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_num = sorted(nums)
        i = 0
        ans = 0
        while i < len(s_num):
            ans += s_num[i]
            i += 2
        return ans