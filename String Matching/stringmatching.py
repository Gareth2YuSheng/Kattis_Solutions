# Author: Gareth Too Yu Sheng
# Problem: String Matching
# Source: https://open.kattis.com/problems/stringmatching

import sys

def build_lps(pat, M, lps):
  i = 1
  j = 0
  while i < M:
    if pat[i] == pat[j]:
      j += 1
      lps[i] = j
      i += 1
    else:
      if j == 0:
        lps[j] = 0
        i += 1
      else:
        j = lps[j-1]

def kmpSearch(txt, pat):
  M = len(pat)
  N = len(txt)
  lps = [0 for _ in range(M)]
  i = 0 # txt[]
  j = 0 # pat[]
  out = []

  build_lps(pat,M,lps)

  while i < N:
    if pat[j] == txt[i]:
      i += 1
      j += 1
    if j == M:
      out.append(str(i-j))
      j = lps[j-1] 
    elif i < N and pat[j] != txt[i]:
      if j > 0:
        j = lps[j-1]
      else:
        i += 1
  return out


def main():  
  while True:
    i = sys.stdin.readline()
    if i == "":
      break
    else:
      print(" ".join(kmpSearch(sys.stdin.readline(), i.strip())))

if __name__ == '__main__':  
    main()

    

    

