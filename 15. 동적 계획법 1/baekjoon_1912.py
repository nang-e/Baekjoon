import sys
n=int(input())
seq=list(map(int,sys.stdin.readline().split()))

d=[0]*n
d[0]=seq[0]

for i in range(1,n):
    d[i]=max(seq[i],seq[i]+d[i-1])
print(max(d))