# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:04:25 2019

@author: DinoBob
"""

class Solution(object):
    def expand(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return l + 1, r - 1
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l0, r0 = 0, 0
        for i in range(0,len(s)-1):
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i+1)
            if r1 - l1 > r0 - l0:
                l0, r0 = l1, r1
            if r2 - l2 > r0 - l0:
                l0, r0 = l2, r2
        return s[l0:r0 + 1]
            
    
ans = Solution()
x = ans.longestPalindrome('aa')