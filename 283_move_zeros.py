# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:27:29 2019

@author: kenzo
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 0:
            if nums[i] != 0:
                break
            i -= 1
        
        j = i - 1
        while j >= 0:
            if nums[j] == 0:
                nums.append(nums.pop(j))
                i -= 1
            j -= 1

ans = Solution().moveZeroes([0,1,0,3,1,2])