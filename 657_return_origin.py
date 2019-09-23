# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:19:40 2019

@author: DinoBob
"""

from collections import defaultdict

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_dict = defaultdict(int)
        for move in moves:
            move_dict[move] += 1
        if (move_dict['U'] == move_dict['D']) and (move_dict['L'] == move_dict['R']):
            return True
        else:
            return False