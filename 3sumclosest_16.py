# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:23:57 2019

@author: DinoBob
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums = ['a'] + nums
        ans = nums[1] + nums[2] + nums[3]
        for i in range(1, len(nums) - 2):
            if nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while k > j:
                s3 = nums[i] + nums[j] + nums[k]
                if abs(s3 - target) < abs(ans - target):
                    ans = s3
                if s3 == target:
                    return s3
                elif s3 > target:
                    k -= 1
                else:
                    j += 1
        return ans
    
ans = Solution()
test = [0,2,1,-3]

x = ans.threeSumClosest(test,1)