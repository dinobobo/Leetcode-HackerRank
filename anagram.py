# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:44:35 2018

@author: DinoBob
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def check_anagram(i, j, s):
    select_dict = defaultdict(int)
    for l in s[i:j]:
        select_dict[l] += 1
    ct = 0    
    for k in range(i+1 , len(s) - j + i +1):
        cmp_dict = defaultdict(int)
        for m in s[k:k+j-i]:
            cmp_dict[m] += 1
        if cmp_dict == select_dict:
            ct += 1
    return ct
            
def anagrams(s):
    if s == None:
        print(0)
        return
    total_ct = 0    
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            total_ct += check_anagram(i,j,s)
    print(total_ct)
    return