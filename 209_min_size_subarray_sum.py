# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:12:48 2019

@author: DinoBob
"""
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0 
        sums = [nums[0]] + (len(nums) - 1)*[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]
            
        ans = len(nums)
        for i in range(len(nums)):
            # sums[mid] - sums[i] + nums[i] > s === sums[mid] > (s + sums[i] - nums[i])
            j = self.search_j(i, len(nums) - 1, sums, s + sums[i] - nums[i])
            if j != -1:
                ans = min(j - i + 1, ans)
        return ans
            
    def search_j(self, l, r, sums, diff):
        while r > l:
            mid = (l + r)//2
            if sums[mid] > diff:
                r = mid
            elif sums[mid] < diff:
                l = mid + 1
            else:
                return mid
        if r == len(sums) - 1 and sums[r] < diff:
            return -1
        else:
            return r
'''

#double pointer
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        i = j = 0
        ans = 2**32 - 1
        current_s = nums[0]
        while i < len(nums):
            if current_s < s and j < len(nums):
                j += 1
                if j < len(nums):
                    current_s += nums[j]
            else:
                if current_s >= s:
                    ans = min(ans, j - i + 1)
                current_s -= nums[i]
                i += 1                
        if ans == 2**32 - 1:
            return 0
        else:
            return ans
        
        
        
x = Solution().minSubArrayLen(11, [1,2,3,4,5])