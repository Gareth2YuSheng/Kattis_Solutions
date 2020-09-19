# Author: Gareth Too Yu Sheng
# Problem: Inverted Deck
# Source: https://open.kattis.com/problems/inverteddeck
# Solution 1

import sys

def main():  
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    sorted_d = sorted(d)
    print(d)
    print(sorted_d)
    
    if d == sorted_d:
      print("1 1")
    else:
      output = []
        
      for end in range(n-1,0,-1):
        for start in range(end+1):
          if (d[:start]+d[start:end+1][::-1]+d[end+1:] == sorted_d):
            output = [start+1,end+1]
            break
        else:
          continue
        break


      if len(output) == 2:
        print(str(output[0])+" "+str(output[1]))
      else:
        print("impossible") 

if __name__ == '__main__':  
    main()