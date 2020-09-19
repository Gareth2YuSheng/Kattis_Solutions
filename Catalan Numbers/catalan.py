# Author: Gareth Too Yu Sheng
# Problem: Catalan Numbers
# Source: https://open.kattis.com/problems/catalan

import sys 

factorial = [1]

for i in range(1,10001):
  factorial.append(factorial[i-1] * i)
    
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  print(factorial[n*2]//(factorial[n+1]*factorial[n]))
