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

class Solution(object):
    def isSubsequence(self, s, t):