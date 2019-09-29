# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:01:54 2019

@author: kenzo
"""

'''
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-2) + self.fib(N-1)
'''
    
#DP:
class Solution(object):
    num = [0,1]
    def fib(self, N):
        l = len(self.num)
        if N < l:
            pass
        elif N - 1 < l:
            self.num.append(self.num[N-2] + self.num[N-1])
        elif N - 2 < l:
            self.num.append(self.num[N - 2] + self.fib(N - 1))
        else:
            self.num.append(self.fib(N-2) + self.fib(N-1))
        return self.num[N]
     