# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:04:43 2018

@author: DinoBob
"""
from collections import defaultdict
def freqQuery(queries):
    db = {}
    keys = defaultdict(int)
    ans = []
    for i in queries:
        if i[0] == 1:
            if i[1] not in db:
                db[i[1]] = 1
                keys[1] += 1
            else:
                db[i[1]] = db[i[1]] + 1
                keys[db[i[1]]] += 1
                keys[db[i[1]] - 1] -= 1
        elif i[0] == 2:
            if i[1] in db:
                if db[i[1]] == 1:
                    db.pop(i[1])
                    keys[1] -= 1                    
                else: 
                    db[i[1]] = db[i[1]] - 1
                    keys[db[i[1]]] += 1
                    keys[db[i[1]] + 1] -= 1 
        else:
            if i[1] in keys.keys() and keys[i[1]] != 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans

with open("C:/Users/kenzo/Desktop/input04.txt") as f:
        content = f.readlines() 
data =  [list(map(int, x.rstrip().split())) for x in content[1:]]
queries = data
ans = freqQuery(queries)

with open("C:/Users/kenzo/Desktop/output04.txt") as f:
        content = f.readlines() 
output =  [list(map(int, x.rstrip().split())) for x in content[:]]
output = [x[0] for x in output]

for i in range(len(ans)):
    if ans[i] != output[i]:
        print(False)