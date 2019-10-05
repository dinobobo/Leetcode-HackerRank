# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:03:37 2019

@author: kenzo
"""

class Solution(object):
    def depthSum(self, nestedList):
        return self.lvl_sum(1, nestedList)
    def lvl_sum(self, lvl, lst):
        res = 0
        for i in lst:
            if i.isInteger() == True:
                res += lvl * (i.getInteger())
            else:
                res += self.lvl_sum(lvl + 1, i.getList())
        return res
