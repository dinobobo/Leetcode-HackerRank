'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        l = len(s)
        while i < l and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == l:
            return True
        else:
            return False
'''

#Using binary search. For a incoming stream of s, it is better to use binary search since we don't have to go through t anymore.

from collections import defaultdict
from bisect import bisect_left
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = defaultdict(list)
        for i, j in enumerate(t):
            dic[j].append(i)
            
          
        k = 0
        for i in s:
            if i not in dic.keys():
                return False
            j = bisect_left(dic[i], k)
            if j == len(dic[i]):
                return False
            else:
                k = dic[i][j] + 1
        return True