# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:59:24 2019

@author: kenzo
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            n = len(nums)
            k = k % n
            drop = nums[n - k:]
            left = nums[: n - k ]
            nums[:k] = drop
            nums[k:] = left
ans  = Solution()
ans.rotate(list(range(1,8)),3)