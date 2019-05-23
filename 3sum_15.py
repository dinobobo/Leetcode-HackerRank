# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:03:36 2019

@author: DinoBob
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = ['a']
        i = 1
        nums = ['a'] + nums
        while i < len(nums) - 2 and nums[i] <= 0:
            if nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1            
            while k > j:
                s3 = nums[i] + nums[j] + nums[k]
                if s3 == 0:                        
                    if [nums[i], nums[j], nums[k]] != ans[-1]:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif s3 > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        ans.pop(0)
        return ans

    
            
            
            
test = [0,0,0,0]
a = Solution()
ans = a.threeSum(test)