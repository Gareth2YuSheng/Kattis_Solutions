# Author: Gareth Too Yu Sheng
# Problem: Faktor
# Source: https://open.kattis.com/problems/faktor

import sys

x, y = list(map(int,sys.stdin.readline().split()))
print(x*(y-1)+1)