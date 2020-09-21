# Author: Gareth Too Yu Sheng
# Problem: Hay Points
# Source: https://open.kattis.com/problems/haypoints

import sys

m, n = tuple(map(int,sys.stdin.readline().split()))
words = {}
for _ in range(m):
  w = sys.stdin.readline().split()
  words[w[0]] = int(w[1])

for _ in range(n):
  salary = 0
  while True:
    i = sys.stdin.readline().split()
    if len(i) == 1 and i[0] == ".":
      print(salary)
      break
    salary += sum(map(lambda w: words[w],[val for val in i if val in words.keys()]))

  

