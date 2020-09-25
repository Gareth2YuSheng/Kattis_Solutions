# Author: Gareth Too Yu Sheng
# Problem: A Different Problem
# Source: https://open.kattis.com/problems/different

import sys

while True:
  i = sys.stdin.readline()
  if i == "":
    break
  else:
    n1,n2 = list(map(int,i.split()))
    print(abs(n1-n2))
