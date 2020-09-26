# Author: Gareth Too Yu Sheng
# Problem: String Matching
# Source: https://open.kattis.com/problems/bijele

import sys

print(" ".join(map(lambda a,b: str(a-b),[1,1,2,2,2,8],list(map(int,sys.stdin.readline().split())))))