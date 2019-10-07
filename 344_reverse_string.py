# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:29:10 2019

@author: DinoBob
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while j > i:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s