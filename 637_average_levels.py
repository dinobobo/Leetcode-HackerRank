# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 07:30:20 2019

@author: kenzo
"""

from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if root:
            tq = deque([[root]])
            while tq:
                node_arr = tq.popleft()
                new_arr = []
                for i in node_arr:
                    if i.left:
                        new_arr.append(i.left)
                    if i.right:
                        new_arr.append(i.right)
                if new_arr:
                    tq.append(new_arr)
                ans.append([i.val for i in node_arr])
        return [sum(i)/len(i) for i in ans]