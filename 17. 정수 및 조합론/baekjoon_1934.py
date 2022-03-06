import sys
def gcf(n,m):
    if n<m: n,m=m,n
    while m>0:
        n,m=m,n%m
    return n
for _ in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    print(int(a*b/gcf(a,b)))