# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:31:42 2019

@author: kenzo
"""

from collections import defaultdict
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        char_d = defaultdict(int)
        for i in chars:
            char_d[i] += 1
        for j in words:
            word_d = defaultdict(int)
            for k in j:
                word_d[k] += 1
            if self.check_include(word_d, char_d):
                ans += len(j)
        return ans
                
    def check_include(self, word_d, char_d):
        for i in word_d.keys():
            if word_d[i] > char_d[i]:
                return False
        return True