# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:41:31 2019

@author: DinoBob
"""

from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.con = deque([])
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.con) < self.size:
            self.con.append(val)
            return sum(self.con)/len(self.con)
        else:
            self.con.popleft()
            self.con.append(val)
            return sum(self.con)/self.size