# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:00:30 2019

@author: DinoBob
"""

import numpy as np
class Solution(object):
    '''
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while a*a <= c:
            b = c - a*a
            l, r = a, b
            while r >= l: 
                mid = int((l+r)/2)
                if mid**2 == b:
                    return True
                elif mid**2 > b:
                    r = mid - 1
                else:
                    l = mid + 1
            a += 1
        return False
    '''
    ### Two pointer for a sorted list ###
    def judgeSquareSum(self, c):
        l, r = 0, int(np.sqrt(c))
        while r >= l:
            if l**2 + r**2 > c:
                r -= 1
            elif l**2 + r**2 < c:
                l += 1
            else:
                return True
        return False
ans = Solution()
x = ans.judgeSquareSum(25)