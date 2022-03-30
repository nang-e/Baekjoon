n,k=map(int,input().split())
d=[[0 for c in range(n+1)] for r in range(n+1)]
d[1][0],d[1][1]=1,1
for i in range(2,n+1):
  for j in range(k+1):
    if j in [0,i]:
      d[i][j]=1
    else:
      d[i][j]=(d[i-1][j]+d[i-1][j-1])%10007
print(d[n][k])

# 그냥 math라이브러리 사용하는 게 더 짧고 편함;,,
import math
a,b = map(int, input().split())

print(math.comb(a,b)%10007)