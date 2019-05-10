# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:09:55 2019

@author: DinoBob
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)
        k = len(num) - 1
        num_new = ''
        while k > 0 :
            if num[k] == 0:
                pass
            else:
                break
            k -= 1
        if x < 0:
            num_new += '-'
            while k > 0 :
                num_new += num[k]
                k -= 1
        else:
            while k >= 0 :
                num_new += num[k]
                k -= 1
        return int(num_new)