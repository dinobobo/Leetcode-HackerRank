# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:56:18 2019

@author: kenzo
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        while r > l:
            mid = (l + r)/2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1

ans = Solution().findMin([2,3,1])