# Author: Gareth Too Yu Sheng
# Problem: Working at the Restaurant
# Source: https://open.kattis.com/problems/restaurant

import sys
from collections import deque

while True:
  n = int(sys.stdin.readline())
  pile1 = deque() #Drop plates here
  pile2 = deque() #Take plates from here
  if n == 0:
    break
  else:
    plate_num = 1
    for _ in range(n):
      action,m = sys.stdin.readline().split()
      m = int(m)
      if action == "DROP":
        print("DROP 1 "+str(m))
        for _ in range(m):
          pile1.append(plate_num)
          plate_num += 1
        
      elif action == "TAKE":
        if len(pile2)==0:
          print("MOVE 1->2 "+str(len(pile1)))
          for _ in range(len(pile1)):
            pile2.append(pile1.pop())
          print("TAKE 2 "+str(m))
          for _ in range(m):
            pile2.pop()
        elif len(pile2) < m:
          remainding = m - len(pile2)
          print("TAKE 2 "+str(len(pile2)))
          for _ in range(len(pile2)):
            pile2.pop()
          print("MOVE 1->2 "+str(len(pile1)))
          for _ in range(len(pile1)):
            pile2.append(pile1.pop())
          print("TAKE 2 "+str(remainding))
          for _ in range(remainding):
            pile2.pop()
        else:
          print("TAKE 2 "+str(m))
          for _ in range(m):
            pile2.pop()
          
    print("")
        
      
        