# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:23:44 2019

@author: kenzo
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]][1] += 1
            else:
                dic[s[i]] = [i, 1]
        ans = []
        for j in dic.values():
            if j[1] == 1:
                ans.append(j[0])
        return min(ans)
    
x  = Solution().firstUniqChar("leetcode")