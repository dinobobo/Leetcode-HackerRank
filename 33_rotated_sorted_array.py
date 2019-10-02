# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:27:55 2019

@author: kenzo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binary_search(0, len(nums), nums, target)
    def binary_search(self, i, j, nums, target):
        if j - i == 1:
            if nums[i] == target:
                return i
            else:
                return -1
        mid = (i + j)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[i] < nums[mid]:
                if nums[i] <= target:
                    ans = self.binary_search(i, mid, nums, target)
                else:
                    if mid + 1 >= j:
                        return -1
                    else:
                        ans = self.binary_search(mid + 1, j, nums, target)
                    
            else:
                ans = self.binary_search(i, mid, nums, target)
                    
        else:
            if nums[i] < nums[mid]:
                if mid + 1 >= j:
                    return -1
                else:
                    ans = self.binary_search(mid + 1, j, nums, target)
            else:
                if nums[j-1] >= target:
                    ans = self.binary_search(mid + 1, j, nums, target)
                else:
                    ans = self.binary_search(i, mid, nums, target)
        return ans