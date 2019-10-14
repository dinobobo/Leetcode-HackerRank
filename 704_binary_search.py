# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:36:33 2019

@author: kenzo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_help(0, len(nums), nums, target)
        
    def search_help(self, i, j, nums, target):
        if i == j:
            return -1
        if i + 1 == j:
            if nums[i] == target:
                return i
            else:
                return -1
        
        mid = (i + j) / 2
        if nums[mid] == target:
            return mid
        else:
            l = self.search_help(i, mid, nums, target)
            r = self.search_help(mid + 1, j, nums, target)
            if l == -1:
                if r == -1:
                    return -1
                else:
                    return r
            else:
                return l