# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:14:42 2019

@author: kenzo
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        res = sum([int(i) for i in str(num)])%9
        if res == 0:
            return 9
        return res
        