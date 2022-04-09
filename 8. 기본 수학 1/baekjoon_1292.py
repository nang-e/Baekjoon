import sys
s=sys.stdin.readline
n,k=map(int,s().split())
lst=list(map(int,s().split()))
lst.sort()
print(lst[k-1])