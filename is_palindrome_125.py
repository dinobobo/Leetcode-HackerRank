# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:20:03 2019

@author: DinoBob
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            while i < len(s) and s[i].isalpha() == False and s[i].isdigit() == False:
                i += 1
            if i == len(s):
                return True
            else: 
                if s[i].isupper():
                    cpi = s[i].lower()
                else:
                    cpi = s[i]
            
            while j >= 0 and s[j].isalpha() == False and s[j].isdigit() == False:
                j -= 1
            if j < 0:
                return True
            else:
                if s[j].isupper():
                    cpj = s[j].lower()
                else:
                    cpj = s[j]
            if cpi == cpj:
                i += 1
                j -= 1
            else:
                return False        
        return True

ans = Solution()
test = "ab2a"
x = ans.isPalindrome(test)