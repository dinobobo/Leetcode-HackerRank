# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:06:54 2019

@author: DinoBob
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = [0]
        mi = 0
        ma = 0
        for i in range(len(prices)):
            if prices[i] > prices[ma]:
                ma = i
            if prices[i] < prices[mi]:
                mi = i
                if ma > mi:
                    ans.append(prices[ma] - prices[mi])
                ma = i
        return max(ans)

ans = Solution()
x = ans.maxProfit([7,1,5,3,6,4])    