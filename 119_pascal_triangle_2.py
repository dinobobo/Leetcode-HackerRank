# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:32:24 2019

@author: kenzo
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = 0
        ans = [0,1,0]
        while k < rowIndex:
            k += 1
            ans = [0] + [ans[i] + ans[i + 1] for i in range(0, len(ans) - 1)] + [0]
        return ans[1:-1]