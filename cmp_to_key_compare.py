# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:51:32 2018

@author: DinoBob
"""
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score       
    def __repr__(self):
        return '{}:{}'.format(self.name,self.score)
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return 1
        
        '''
        if self.score > other.score:
            return True
        elif self.score < other.score:
            return False
        else:
            return self.name < other.name
        ''' 
a = Player('c',1)
b = Player('e',2)
c = Player('d',2)
ans = sorted([c,a,b], key = cmp_to_key(Player.comparator))
print(ans)