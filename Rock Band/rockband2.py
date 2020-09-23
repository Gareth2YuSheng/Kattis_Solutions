# Author: Gareth Too Yu Sheng
# Problem: Rock Band
# Source: https://open.kattis.com/problems/rockband

import sys

m, s = list(map(int,sys.stdin.readline().split()))
last_occurence = [0 for _ in range(s)]

# METHOD 1: storing songs as a songlist e.g. [[2,5,4,8,1,6,3,7],...]
# songs = []
# for _ in range(m):
#   songlist = list(map(int,sys.stdin.readline().split()))
#   songs.append(songlist)
#   for x in songlist:
#     if last_occurence[x-1] < songlist.index(x):
#       last_occurence[x-1] = songlist.index(x)

# r = 0
# while r < s-1:
#   rank = songs[r]
#   last = max(map(lambda a: last_occurence[a-1],rank))
#   if r == last:
#     break
#   else:
#     r = last 

# result = sorted(songs[0][:r+1])
# print(result)
# print(len(result))
# for i in result:
#   print(str(i)+" ", end='')

# METHOD 2: storning songs by rank e.g. [[4,5,2],[5,2,5],[2,4,4],...]
songs = [[] for _ in range(s)]
for _ in range(m):
  songlist = list(map(int,sys.stdin.readline().split()))
  for x in range(s):
    songs[x].append(songlist[x])
    if last_occurence[songlist[x]-1] < songlist.index(songlist[x]):
      last_occurence[songlist[x]-1] = songlist.index(songlist[x])

r = 0
while r < s-1:
  rank = songs[r]
  last = max(map(lambda a: last_occurence[a-1],rank))
  if r == last:
    break
  else:
    r = last 
r+=1

print(r)
result = [songs[i][0] for i in range(r)]
result.sort()
# print(result)
for i in result:
  print(str(i)+" ", end='')
