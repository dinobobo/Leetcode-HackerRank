# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 06:24:07 2019

@author: kenzo
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right+1):
            div, rem = divmod(x, 10)
            if rem == 0 or x % rem != 0:
                continue
            while div != 0 and rem != 0 and x % rem == 0:
                    div, rem = divmod(div, 10)
            if div == 0 and x % rem == 0:
                res.append(x)
        return res
    
ans = Solution()
x = ans.selfDividingNumbers(10,22)