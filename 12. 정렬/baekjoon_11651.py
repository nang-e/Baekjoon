import sys
s=sys.stdin.readline
n=int(s())
c=[list(map(int,s().split())) for _ in range(n)]

c.sort(key=lambda x: [x[1],x[0]])

for i in c:
  print(i[0],i[1])