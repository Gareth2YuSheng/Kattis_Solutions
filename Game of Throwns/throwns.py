# Author: Gareth Too Yu Sheng
# Problem: Game of Throwns
# Source: https://open.kattis.com/problems/throwns

import sys
from collections import deque

n, k = list(map(int,sys.stdin.readline().split()))
comms = sys.stdin.readline().split()
execute_comms = deque()

c = 0
while c < len(comms):
  if comms[c] == "undo":
    c+=1
    for _ in range(int(comms[c])):
      execute_comms.pop() 
  else:
    execute_comms.append(int(comms[c]))
  c+=1

print(sum(execute_comms)%n)
