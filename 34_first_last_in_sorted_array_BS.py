# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:50:28 2019

@author: DinoBob
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        l = self.find_left_extreme(nums, target)
        if nums[l] != target:
            return [-1,-1]
        r = self.find_right_extreme(nums, target)
        if nums[r + 1] == target:
            r += 1
        return [l,r]
    
    def find_left_extreme(self, nums, target):
        l = 0
        r = len(nums) - 1
        while r > l:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
        
    def find_right_extreme(self, nums, target):
        l = 0
        r = len(nums) - 1
        while r > l:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r - 1 
x = Solution().searchRange([1,1,1,1,2,3,3,3], 3)