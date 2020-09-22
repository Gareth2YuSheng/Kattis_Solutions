# Author: Gareth Too Yu Sheng
# Problem: Inverted Deck
# Source: https://open.kattis.com/problems/inverteddeck

import sys

def main():  
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    sorted_d = sorted(d)
    
    if d == sorted_d:
      print("1 1")
    else:
      start = 0
      end = n-1

      for i in range(n):
        if d[i] != sorted_d[i]:
          start = i
          break
      for i in range(n-1,-1,-1):
        if d[i] != sorted_d[i]:
          end = i
          break

      if d[:start]+d[start:end+1][::-1]+d[end+1:] == sorted_d:
        print(str(start+1)+" "+str(end+1))
      else:
        print("impossible")

if __name__ == '__main__':  
    main()