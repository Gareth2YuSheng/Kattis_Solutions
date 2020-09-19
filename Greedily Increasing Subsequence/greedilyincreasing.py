# Author: Gareth Too Yu Sheng
# Problem: Greedily Increasing Subsequence       
# Source: https://open.kattis.com/problems/greedilyincreasing                                                            

import sys

num = sys.stdin.readline()
i = sys.stdin.readline()
i = i[:len(i)-1].split(" ")
o = [i[0]]

for x in range(1,len(i)):
    if int(i[x]) > int(o[-1]):
        o.append(i[x])

print(len(o))
print(" ".join(o))

                                      