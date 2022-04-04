import sys
s=sys.stdin.readline
n=int(s())
lst=[int(s()) for _ in range(n)]

dp=[0]*10000
dp[0]=lst[0]
for i in range(1,n):
    if i==1:
        dp[1]=dp[0]+lst[1]
    else:
        dp[i]=max(dp[i-1],dp[i-3]+lst[i-1]+lst[i],dp[i-2]+lst[i])
print(dp[n-1])