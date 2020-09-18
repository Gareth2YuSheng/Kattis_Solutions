# Author: Gareth Too Yu Sheng
# Problem: Cetvrta
# Source: https://open.kattis.com/problems/cetvrta

import sys

x_pos, y_pos = [],[]

for _ in range(3):
  x,y = sys.stdin.readline().split()
  x_pos.append(int(x))
  y_pos.append(int(y))

print("{} {}".format(min(x_pos,key=x_pos.count),min(y_pos,key=y_pos.count)))