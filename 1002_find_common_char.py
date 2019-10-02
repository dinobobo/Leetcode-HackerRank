# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:19:12 2019

@author: DinoBob
"""

from collections import defaultdict
class Solution:
    def commonChars(self, A):
        dic = []
        for i in A:
            sub_dic = defaultdict(int)
            dic.append(sub_dic)
            for j in i:
                sub_dic[j] += 1
                
                
        ans = []
        for k in dic[0].keys():
            ct = dic[0][k]
            for l in dic[1:]:
                if k not in l:
                    ct = 0
                    break
                else:
                    ct = min(ct, l[k])
            ans += [k for _ in range(ct)]
        return ans

x = Solution().commonChars(["bella","label","roller"])