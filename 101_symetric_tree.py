# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:31:10 2019

@author: kenzo
"""

from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            lq = deque([root.left])
            rq = deque([root.right])
            while lq and rq:
                node_l = lq.popleft()
                node_r = rq.popleft()
                if node_l and node_r:
                    if node_l.val != node_r.val:
                        return False
                    else:
                        lq.append(node_l.left)
                        lq.append(node_l.right)
                        rq.append(node_r.right)
                        rq.append(node_r.left)
                        
                elif not node_l and not node_r:
                    pass
                else:
                    return False
            if lq or rq:
                return False
            else:
                return True
        
        else:
            return True