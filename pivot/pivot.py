# Author: Gareth Too Yu Sheng
# Problem: Pivot
# Source: https://open.kattis.com/problems/pivot
# Solution 1

import sys

def main():  
    num = int(sys.stdin.readline())
    i = [int(n) for n in sys.stdin.readline().split()]
    count = 0

    for n,e in enumerate(i):
      if n > 0:
        if e < max(i[:n]):
          continue
      if n < num-1:
        if e > min(i[n+1:]):
          continue
      count += 1

    print(count)  

if __name__ == '__main__':  
    main()

