# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:27:49 2019

@author: DinoBob
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        Ugly number using DP
        """
        ugly = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(ugly) < n:
            umin = min([ugly[i2]*2, ugly[i3]*3, ugly[i5]*5])
            if ugly[i2]*2 == umin:
                i2 += 1
            if ugly[i3]*3 == umin:
                    i3 += 1
            if ugly[i5]*5 == umin:
                    i5 += 1
            ugly.append(umin)
        return ugly[-1]

ans = Solution()
a = ans.nthUglyNumber(10)