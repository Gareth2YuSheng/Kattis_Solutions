# Author: Gareth Too Yu Sheng
# Problem: I've Been Everywhere, Man
# Source: https://open.kattis.com/problems/everywhere

import sys

for _ in range(int(sys.stdin.readline())):
  s = set()
  for _ in range(int(sys.stdin.readline())):
    s.add(sys.stdin.readline())
  print(len(s))