import sys
s=sys.stdin.readline
n=int(s())
load=list(map(int,s().split()))
price=list(map(int,s().split()))

ans,c=0,1000000001
for i in range(n-1):
  c=min(c,price[i])
  ans+=c*load[i]
print(ans)