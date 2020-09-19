# Author: Gareth Too Yu Sheng
# Problem: Battle Simulation
# Source: https://open.kattis.com/problems/battlesimulation

import sys

i = list(sys.stdin.readline())[:-1]
c = 0

while c < len(i):
    if (c<len(i)-2 and i[c]!=i[c+1] and i[c]!=i[c+2] and i[c+2]!=i[c+1]):
        print('C', end='')
        c+=3
        continue
    elif i[c] == "R":
        print('S', end='')
    elif i[c] == "B":
        print('K', end='')
    elif i[c] == "L":
        print('H', end='')
    c+=1