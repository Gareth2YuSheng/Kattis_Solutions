# Author: Gareth Too Yu Sheng
# Problem: Flipping Patties
# Source: https://open.kattis.com/problems/flippingpatties

import sys
import math

n = int(sys.stdin.readline())
time = [0 for _ in range(43201)]
for _ in range(n):
  d,t = map(int, sys.stdin.readline().split())
  time[t] += 1 #finish cooking and remove patty
  time[t-d] += 1 #flip patty
  time[t-d*2] += 1 #add new patty

print(int(math.ceil(max(time)/2)))
  
