# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:30:44 2018

@author: DinoBob
"""


from collections import defaultdict


def find_med(freq, d):
    num = 0
    for i in range(201):
        num += freq[i]
        if num > d//2:
            return i



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    ct = 0
    freq = defaultdict(int)
    for i in expenditure[:d]:
        freq[i] += 1
    if d%2 == 1:
        for j in range(d,len(expenditure)):
            med = find_med(freq, d)
            freq[expenditure[j]] += 1
            freq[expenditure[j - d]] -= 1
            if expenditure[j] >= 2*med:
                ct += 1
    else:
        for j in range(d,len(expenditure)):
            med_l = find_med(freq, d)
            med_s = find_med(freq,d-1)
            freq[expenditure[j]] += 1
            freq[expenditure[j - d]] -= 1
            if expenditure[j] >= med_l + med_s:
                ct += 1
    return ct



test = [2,3,4,2,3,6,8,4,5]    

ans = activityNotifications(test,5)