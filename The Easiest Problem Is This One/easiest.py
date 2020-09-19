# Author: Gareth Too Yu Sheng
# Problem: The Easiest Problem is This One
# Source: https://open.kattis.com/problems/easiest

import sys

while True:
  i = sys.stdin.readline()
  if int(i) == 0:
    break
  else:
    p = 11
    n = int(i)
    sum_n = sum(int(d) for d in i[:-1])
    while True:
      if sum(int(d) for d in str(p*n)) == sum_n:
        print(p)
        break
      else:
        p+=1
