# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:00:18 2019

@author: kenzo
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        else:
            ans = [[0,1,0]]
            while len(ans) < numRows:
                ans.append([0] + [ans[-1][i] + ans[-1][i + 1] for i in range(len(ans[-1]) - 1)] + [0])    
        return [i[1:-1] for i in ans]
    
ans = Solution()
x = ans.generate(5)