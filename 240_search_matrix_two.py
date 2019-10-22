# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:31:53 2019

@author: DinoBob
"""
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix == []:
            return False
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
'''

import numpy as np
from bisect import bisect_left
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        matrix = np.array(matrix)
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        return self.searchSubM(l, r, t, b, matrix, target)
        
    def searchSubM(self, l, r, t, b, matrix, target):
        if r < l or b < t:
            return False
        elif matrix[t,l] > target or matrix[b, r] < target:
            return False
        
        midx = (l + r)//2
        midy = bisect_left(matrix[t: b + 1, midx], target) + t
        if midy <= b and matrix[midy, midx] == target:
            return True      
        return self.searchSubM(l, midx - 1, midy, b, matrix, target) or self.searchSubM(midx + 1, r, t, midy - 1, matrix, target)
    
x = Solution().searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]],13)