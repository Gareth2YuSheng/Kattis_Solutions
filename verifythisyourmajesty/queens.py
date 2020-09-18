# Author: Gareth Too Yu Sheng
# Problem: Verify This, Your Majesty
# Source: https://open.kattis.com/contests/q8rr4g/problems/queens


import sys

n = int(sys.stdin.readline())
x_pos = []
y_pos = []
r_diagonals = []
l_diagonals = []

# check for right diagonal do x - y and compare
# check for left diagonal do x + y and compare

for _ in range(n):
  x,y = map(int, sys.stdin.readline().split())
  x_pos.append(x)
  y_pos.append(y)
  r_diagonals.append(x-y)
  l_diagonals.append(x+y)

# check horizontally
if len(set(x_pos)) != len(x_pos):
  print("INCORRECT")
# check vertically
elif len(set(y_pos)) != len(y_pos):
  print("INCORRECT")
# check diagonally
elif len(set(r_diagonals)) != len(r_diagonals): #right
  print("INCORRECT")
elif len(set(l_diagonals)) != len(l_diagonals): #left
  print("INCORRECT")
# else
else:
 print("CORRECT")


