# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:42:46 2018

@author: DinoBob
"""

#!/bin/python3
import csv
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    ct = 0
    lt = defaultdict(int)
    rt = defaultdict(int)
    for i in arr[1:len(arr)]:
        rt[i] += 1
    for j in range(len(arr) - 1):
        ct += lt[arr[j]/r]*rt[arr[j]*r]
        lt[arr[j]] += 1
        rt[arr[j+1]] -= 1        
    return ct


if __name__ == '__main__':  
    with open("C:/Users/kenzo/Desktop/input11.txt") as f:
        content = f.readlines()
    nr = content[0].rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, content[1].rstrip().split()))
    ans = countTriplets(arr, r)

        
        
        
