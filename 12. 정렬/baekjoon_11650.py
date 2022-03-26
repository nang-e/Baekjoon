import sys
s=sys.stdin.readline
n=int(s())
coord=[list(map(int,s().split())) for _ in range(n)]

coord.sort(key=lambda x: (x[0],x[1]))

for i in coord:
  print(i[0],i[1])