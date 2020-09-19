# Author: Gareth Too Yu Sheng
# Problem: 3D Printed Statues
# Source: https://open.kattis.com/problems/3dprinter

import sys

base2 = [2**x for x in range(15)]

i = int(sys.stdin.readline())

for x in base2:
  if i <= x:
    print(base2.index(x)+1)
    break
