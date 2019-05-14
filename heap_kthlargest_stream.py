# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:04:43 2019

@author: DinoBob
"""

from heapq import heapify, heappush, heappushpop, heappop
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        heapify(nums)
        if self.k < len(nums):
            while len(nums) > k:
                heappop(nums)
            self.pq = nums
        else:
            self.pq = nums
            
                                    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """ 
        if self.k <= len(self.pq):
            if val > self.pq[0]:
                heappushpop(self.pq, val)
                return self.pq[0]
            else:
                return self.pq[0]
        else:
            heappush(self.pq, val)
            return self.pq[0]

        
        
ans = KthLargest(3,[4,5,8,2])
test = [3,5,10,9,4]
for i in test:
    print(ans.add(i))
