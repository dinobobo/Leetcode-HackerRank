# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:21:22 2019

@author: kenzo
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Compute the max subarray ending at index i, and the max subarray ending at i + 1
        # Should be max(max_sub[i] + nums[i + 1], nums[i + 1]), then compare all the max               # ending at different indices
    
        sub_max = nums[0]
        total_max = nums[0]
        for i in nums[1:]:
                sub_max = max(sub_max + i, i)
                total_max = max(sub_max, total_max)
        return total_max