# Author: Gareth Too Yu Sheng
# Problem: Eb Alto Saxophone Player
# Source: https://open.kattis.com/problems/saxophone

import sys

for _ in range(int(sys.stdin.readline())):
  fingers = [0 for _ in range(10)]
  presses = [0 for _ in range(10)]
  song = sys.stdin.readline().strip()
  # print(song)
  for note in song:
    # print(note+":")
    if note == "c":
      for f in range(len(fingers)):
        if (f>=1 and f<=3) or (f>=6 and f<=9):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "d":
      for f in range(len(fingers)):
        if (f>=1 and f<=3) or (f>=6 and f<=8):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "e":
      for f in range(len(fingers)):
        if (f>=1 and f<=3) or f==6 or f==7:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "f":
      for f in range(len(fingers)):
        if (f>=1 and f<=3) or f==6:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "g":
      for f in range(len(fingers)):
        if (f>=1 and f<=3):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "a":
      for f in range(len(fingers)):
        if f==1 or f==2:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "b":
      for f in range(len(fingers)):
        if f==1:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "C":
      for f in range(len(fingers)):
        if f==2:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "D":
      for f in range(len(fingers)):
        if (f>=0 and f<=3) or (f>=6 and f<=8):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "E":
      for f in range(len(fingers)):
        if (f>=0 and f<=3) or f==6 or f==7:
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "F":
      for f in range(len(fingers)):
        if (f>=0 and f<=3) or f==6 :
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "G":
      for f in range(len(fingers)):
        if (f>=0 and f<=3):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "A":
      for f in range(len(fingers)):
        if (f>=0 and f<=2):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    elif note == "B":
      for f in range(len(fingers)):
        if (f>=0 and f<=1):
          if fingers[f] == 0:
            fingers[f] = 1
            presses[f] += 1
        elif fingers[f] == 1:
          fingers[f] = 0
    # print(fingers)
    # print(presses)
  print(" ".join([str(x) for x in presses]))

