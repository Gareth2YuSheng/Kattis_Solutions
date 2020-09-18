# Author: Gareth Too Yu Sheng
# Problem: Parking
# Source: https://open.kattis.com/problems/parking

import sys

rates = list(map(int,sys.stdin.readline().split()))
trucks = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]
cost = 0
parked_trucks = 0

for t in range(1,100):
  #if truck enters
  if t == trucks[0][0]:
    parked_trucks += 1
  if t == trucks[1][0]:
    parked_trucks += 1
  if t == trucks[2][0]:
    parked_trucks += 1
  #if truck leaves
  if t == trucks[0][1]:
    parked_trucks -= 1
  if t == trucks[1][1]:
    parked_trucks -= 1
  if t == trucks[2][1]:
    parked_trucks -= 1
  cost += rates[parked_trucks-1]*parked_trucks
  
print(cost)