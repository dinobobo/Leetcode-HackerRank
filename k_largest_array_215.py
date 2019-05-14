# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:07:09 2019

@author: DinoBob
"""

from heapq import heapify, heappushpop
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapify(min_heap)
        for i in nums[k:]:
            if i > min_heap[0]:
                heappushpop(min_heap, i)
        return min_heap[0]
    
ans = Solution()
print(ans.findKthLargest([2,1], 2))