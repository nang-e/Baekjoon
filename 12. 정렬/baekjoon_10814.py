import enum


import sys
s=sys.stdin.readline
n=int(s())
lst=[s().split() for i in range(n)]

lst.sort(key=lambda x:int(x[0]))

for i in lst:
  print(i[0],i[1])