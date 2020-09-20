# Author: Gareth Too Yu Sheng
# Problem: 2048
# Source: https://open.kattis.com/problems/2048

import sys

grid = [ list(map(int,sys.stdin.readline().split())) for _ in range(4) ]
action = int(sys.stdin.readline())
'''
0 - left
1- up
2 - right
3 - down
'''
# print(grid)
# print(action)


def swipe(row):
  if len(set(row)) == len(row) and 0 not in row:
    # skip row if no empty spaces and all numbers are unique
    return row
  else:
    row[:] = (value for value in row if value != 0)
    for n in range(len(row)-1):
      if row[n] == row[n+1]:
        row[n] *= 2
        row[n+1] = 0 
    row[:] = (value for value in row if value != 0)
    row.extend([0 for _ in range(4-len(row))])
  return row

if action == 0:
  for x in range(4):
    grid[x] = swipe(grid[x])
elif action == 1:
  for x in range(4):
    temp_list = [grid[0][x],grid[1][x],grid[2][x],grid[3][x]]
    temp_list = swipe(temp_list)
    grid[0][x],grid[1][x],grid[2][x],grid[3][x] = temp_list[0],temp_list[1],temp_list[2],temp_list[3]
elif action == 2:
  for x in range(4):
    grid[x].reverse()
    grid[x] = swipe(grid[x])
    grid[x].reverse()
elif action == 3:
  for x in range(4):
    temp_list = [grid[3][x],grid[2][x],grid[1][x],grid[0][x]]
    temp_list = swipe(temp_list)
    grid[0][x],grid[1][x],grid[2][x],grid[3][x] = temp_list[3],temp_list[2],temp_list[1],temp_list[0]

for x in grid:
  print(" ".join([str(int) for int in x]))