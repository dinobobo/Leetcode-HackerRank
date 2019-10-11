# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:19:37 2019

@author: kenzo
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(len(s) - 1):
            if s[i: i + 2] == "++":
                ans.append(s[:i] + "--" + s[i + 2 :])
        return ans

x = Solution().generatePossibleNextMoves("++++")