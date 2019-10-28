# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:31:06 2019

@author: DinoBob
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        i = 1
        if n < 0:
            x = 1.0/x
            n = -n
        while n != 0:
            if n % 2:
                ans *= x**(i)
            i *= 2
            n = n // 2
        return ans