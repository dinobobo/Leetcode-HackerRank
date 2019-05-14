# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:55:06 2019

@author: DinoBob
"""
'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        pts = [0 for i in range(len(primes))]
        while n > 1:
            umin = min([ugly[a]*b for a, b in zip(pts, primes)])
            for k in range(len(pts)):
                if ugly[pts[k]]*primes[k] == umin:
                    pts[k] += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
    
'''

#####Using a Heap#####
from heapq import heapify, heappush, heappop
def nthSuperUglyNumber(n,primes):
    ugly = [1]
    pool = []
    for i in range(len(primes)):
        pool.append([primes[i],0,primes[i]])
    heapify(pool)
    while n > 1:
        val, idx, p = heappop(pool)
        if val != ugly[-1]:
            n -= 1
            ugly.append(val)
        heappush(pool, [ugly[idx + 1]*p, idx+1, p])
    return ugly[-1]





a = nthSuperUglyNumber(10, [2,3,5])
                    
