# Author: Gareth Too Yu Sheng
# Problem: Even Up Solitaire
# Source: https://open.kattis.com/problems/evenup

import sys
from collections import deque

n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

myStack = deque()

for c in range(n):
  myStack.append(cards[c])
  if len(myStack) > 1:
    if (myStack[-2] + myStack[-1])%2 == 0:
      myStack.pop()
      myStack.pop()

print(len(myStack))
  