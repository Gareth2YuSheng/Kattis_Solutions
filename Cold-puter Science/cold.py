# Author: Gareth Too Yu Sheng
# Problem: Cold-puter Science
# Source: https://open.kattis.com/problems/cold

import sys

n = int(sys.stdin.readline())
temps = list(map(int,sys.stdin.readline().split()))
print(len([val for val in temps if val < 0]))