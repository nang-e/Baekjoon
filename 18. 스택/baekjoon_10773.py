import sys
s=sys.stdin.readline
k=int(s())
lst=[]
for _ in range(k):
    i=int(s())
    lst.append(i) if i else lst.pop()
print(sum(lst))