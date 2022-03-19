import sys
s=sys.stdin.readline
n=int(s())
d=[list(map(int,s().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(len(d[i])):
    if j==0:
      d[i][j]+=d[i-1][j]
    elif j==(len(d[i])-1):
      d[i][j]+=d[i-1][j-1]
    else:
      d[i][j]+=max(d[i-1][j-1],d[i-1][j])

print(max(d[n-1]))