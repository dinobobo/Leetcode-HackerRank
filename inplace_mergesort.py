# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 09:15:56 2018

@author: DinoBob
"""
def countInversions(arr,start, end):
    if start == end:
        return 0
    sp_l = countInversions(arr, start, (end+start)//2)
    sp_r = countInversions(arr, (end+start)//2 + 1, end)
    sort_temp = []
    j = start
    k = (end+start)//2 + 1
    swap = 0
    while len(sort_temp) < end - start + 1:
        if arr[k] < arr[j]:
            sort_temp.append(arr[k])
            k += 1
            swap += (end+start)//2 - j + 1
            if k > end:
                sort_temp += arr[j:(end+start)//2 + 1]
                break
        else:
            sort_temp.append(arr[j])
            j += 1
            if j > (end+start)//2:
                sort_temp += arr[k:end + 1]
                break
    arr[start:end + 1] = sort_temp
    return swap + sp_l + sp_r

test = [2,1,3,1,2,1,1]
ans = countInversions(test,0,len(test)-1)