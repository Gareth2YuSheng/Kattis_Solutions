# Author: Gareth Too Yu Sheng
# Problem: Rock Band
# Source: https://open.kattis.com/problems/rockband

import sys

m, s = list(map(int,sys.stdin.readline().split()))

songs = [[] for _ in range(s)]
for _ in range(m):
  songlist = list(map(int,sys.stdin.readline().split()))
  for x in range(s):
    songs[x].append(songlist[x])

def compute(songs):
  counts = [0 for _ in range(s)]
  for rank in range(s):
    for x in songs[rank]:
      counts[x-1] += 1
      if set(counts)=={0,m}:
        results = [str(i+1) for i, e in enumerate(counts) if e == m]
        print(len(results))
        print(" ".join(results))
        return
  print(s)
  print(" ".join([str(i+1) for i in range(s)]))
  
compute(songs)


