# Author: Gareth Too Yu Sheng
# Problem: Pivot
# Source: https://open.kattis.com/problems/pivot

import sys

def main():  
    num = int(sys.stdin.readline())
    i = list(map(int, sys.stdin.readline().split()))
    count = 0
    maxes = [0 for _ in range(num)]
    mins = [2**32 - 1 for _ in range(num)] 

    for x in range(1, num):  
      maxes[x] = max(maxes[x-1], i[x-1])
    for x in range(num-2, -1, -1):  
      mins[x] = min(mins[x+1], i[x+1])
    for x in range(num):
      if i[x] >= maxes[x] and i[x] < mins[x]:
        count+=1

    print(count)  

if __name__ == '__main__':  
    main()

