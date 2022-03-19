import sys
s=sys.stdin.readline
n=int(s())
d=[list(map(int,s().split())) for _ in range(n)]

for i in range(1,n):
  d[i][0]+=min(d[i-1][1],d[i-1][2])
  d[i][1]+=min(d[i-1][0],d[i-1][2])
  d[i][2]+=min(d[i-1][0],d[i-1][1])
  
print(min(d[n-1]))