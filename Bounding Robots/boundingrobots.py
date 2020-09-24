# Author: Gareth Too Yu Sheng
# Problem: Bounding Robots
# Source: https://open.kattis.com/problems/boundingrobots

import sys

while True:
  think_pos = [0,0]
  actual_pos = [0,0]
  w, l = list(map(int,sys.stdin.readline().split()))
  if w==0 and l==0:
    break
  i = int(sys.stdin.readline())
  for _ in range(i):
    d,v = sys.stdin.readline().split()
    v = int(v)
    if d == 'u':
      think_pos[1] += v
      actual_pos[1] += v
      if actual_pos[1] > l-1:
        actual_pos[1] = l-1
    elif d == 'r':
      think_pos[0] += v
      actual_pos[0] += v
      if actual_pos[0] > w-1:
        actual_pos[0] = w-1
    elif d == 'l':
      think_pos[0] -= v
      actual_pos[0] -= v
      if actual_pos[0] < 0:
        actual_pos[0] = 0
    elif d == 'd':
      think_pos[1] -= v
      actual_pos[1] -= v
      if actual_pos[1] < 0:
        actual_pos[1] = 0
  print("Robot thinks {} {}".format(think_pos[0],think_pos[1]))
  print("Actually at {} {}\n".format(actual_pos[0],actual_pos[1]))
  