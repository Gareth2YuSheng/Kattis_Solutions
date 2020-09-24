# Author: Gareth Too Yu Sheng
# Problem: Pairing Socks
# Source: https://open.kattis.com/problems/pairingsocks

import sys
from collections import deque

n = int(sys.stdin.readline())
socks = deque(map(int,sys.stdin.readline().split()))
socks.reverse()
aux = deque()
moves = 0

while len(socks) > 0:
  if len(socks) > 0 and len(aux) > 0 and socks[-1] == aux[-1]:
    socks.pop()
    aux.pop()
  else:
    aux.append(socks.pop())
  moves += 1

if not len(aux) and not len(socks):
  print(moves)
else:
  print("impossible")