# Author: Gareth Too Yu Sheng
# Problem: Statistics
# Source: https://open.kattis.com/problems/statistics

import sys

cases = []

for c in range(10):
    i = sys.stdin.readline()
    if i == '':
        break
    else:
        cases.append([int(x) for x in i[:len(i)-1].split(" ")][1:])
        
for c in range(len(cases)):
    print("Case "+str(c+1)+": "+str(min(cases[c]))+" "+str(max(cases[c]))+" "+str(max(cases[c])-min(cases[c])))
