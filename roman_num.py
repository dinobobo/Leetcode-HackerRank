# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:52:11 2019

@author: DinoBob
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    num += table[s[i+1]] - 1
                    i += 2
                else:
                    num += 1
                    i += 1                    
            elif s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    num += table[s[i+1]] - 10
                    i += 2
                else:
                    num += 10
                    i += 1
            elif s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    num += table[s[i+1]] - 100
                    i += 2
                else:
                    num += 100
                    i += 1
            else:
                num += table[s[i]]
                i += 1
        if i == len(s):
            return num
        else:
            return num + table[s[-1]]
so = Solution()
so.romanToInt('DCXXI')