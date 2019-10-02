# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:20:08 2019

@author: kenzo
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.add_subset(ans, nums, [], 0)
        return ans
        
    def add_subset(self, ans, nums, so_far, i):
        if i < len(nums) + 1:
            ans.append(so_far)
            for j in range(i, len(nums)):
                self.add_subset(ans, nums, so_far + [nums[j]], j + 1)
        return ans

ans = Solution()
x = ans.subsets([1,2,3])