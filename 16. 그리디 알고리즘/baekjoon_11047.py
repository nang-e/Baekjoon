import sys
n,k=map(int,input().split())

lst=[int(sys.stdin.readline()) for _ in range(n)]
lst.reverse()

c=0
for i in lst:
    if i<=k: c+=k//i; k%=i
    if k==0: break
print(c)