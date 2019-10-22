# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:36:03 2019

@author: kenzo
"""

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while r >= l:
            mid = (l + r)/2
            if isBadVersion(mid) == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    r = mid - 1
            else:
                if isBadVersion(mid + 1) == True:
                    return mid + 1
                else:
                    l = mid + 1