# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:58:44 2019

@author: kenzo
"""

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while n > 0:
            buf4 = [""]*4
            l = read4(buf4)
            if not l:
                return i
            for k in range(min(l, n)):
                buf[i] = buf4[k]
                i += 1
                n -= 1
        return i