# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:44:27 2019

@author: kenzo
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        if not digits:
            return ""
        
        if len(digits) == 1:
            return [i for i in dic[digits[0]]]
        ans = []
        for i in dic[digits[0]]:
            for j in self.letterCombinations(digits[1:]):
                ans.append(i + j)
        return ans