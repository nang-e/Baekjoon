import sys
s=sys.stdin.readline
T=int(s())

d=[0]*101
d[0],d[1],d[2],d[3],d[4],d[5]=0,1,1,1,2,2
for _ in range(T):
    n=int(s())
    for i in range(6,n+1):
        d[i]=d[i-1]+d[i-5]
    print(d[n])