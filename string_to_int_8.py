# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:27:29 2019

@author: DinoBob
"""
from collections import defaultdict
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        intdic = defaultdict(int)
        for i in range(10):
            intdic[str(i)]
        dic = intdic.copy()
        dic['+']
        dic['-']

        i = 0
        while i < len(s) and s[i] ==' ':
            i += 1
        if i < len(s) and s[i] in dic:
            if s[i] == '-' or s[i] == '+':
                if i == len(s) - 1:
                    return 0
                else:
                    j = i + 1
                    while j < len(s) and s[j] in intdic:
                        j += 1
                    if j - i == 1:
                        return 0
                    elif int(str(s[i:j])) > 2**31 - 1:
                        return 2**31 -1
                    elif int(str(s[i:j])) < -2**31:
                        return -2**31 
                    else:
                        return int(str(s[i:j]))
            else:
                j = i + 1
                while j < len(s) and s[j] in intdic:
                    j += 1
                if int(str(s[i:j])) > 2**31 - 1:
                    return 2**31 -1
                elif int(str(s[i:j])) < -2**31:
                    return -2**31 
                else:
                    return int(str(s[i:j]))           
        else:
            return 0
            
        
            
    

ans = Solution()

x = ans.myAtoi('-abc')
