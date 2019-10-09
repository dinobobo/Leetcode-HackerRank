# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:52:37 2019

@author: DinoBob
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        while j < len(nums):
            if nums[j] == nums[i]:
                if j - i > 1:
                    nums.pop(j)
                else:
                    j += 1
            
            else:
                i = j
                j += 1