# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:29:00 2019

@author: kenzo
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [i - j for i, j in zip(gas,cost)]
        tank = 0
        total = 0
        stop = 0
        i = 0
        while i < len(gas):
            tank += diff[i]
            total += diff[i]
            if tank < 0:
                tank = 0
                stop  = i + 1
            i += 1
        if total < 0: return -1
        if stop == len(gas):
            return -1
        else:
            return stop
ans = Solution()
x = ans.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])