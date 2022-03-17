# 시간초과
def f(n):
    i,ans=1,1
    while i<=n:
        ans*=i
        i+=1
    return ans

n=int(input())
cnt,s=0, 1 if n%2 else 0
for i in range(s,n+1,2):
    j=int((n-i)/2)
    cnt+=f(i+j)/(f(i)*f(j))
print(int(cnt%15746))

# Dynamic Programming
n=int(input())
d=[0]*1000001
d[1],d[2]=1,2
for i in range(3,n+1):
    d[i]=(d[i-1]+d[i-2])%15746
print(d[n])